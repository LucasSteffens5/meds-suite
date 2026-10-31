#!/usr/bin/env python3
"""Executa casos fictícios em sessões novas de um harness CLI e exige revisão humana."""

import argparse
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harnesses


ROOT = Path(__file__).resolve().parents[1]
SKILL = harnesses.SKILL


def snapshot(folder):
    return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob("*")) if p.is_file()
            and ".result" not in p.relative_to(folder).parts}


def run_case(suite, output, scenario, repetition, cli_version, installed_plugin=False,
             plugin_version=None, harness="codex", model=None, plan_file=None):
    folder = output / f"{scenario['id']}-{repetition}"
    folder.mkdir()
    harnesses.install_skill(suite, folder, harness, installed_plugin)
    plan_input = None
    if scenario["plan"]:
        source_plan = Path(plan_file) if plan_file else ROOT / "tests/behavior" / scenario["plan"]
        plan = source_plan.read_text(encoding="utf-8")
        (folder / "plano-meds.md").write_text(plan + scenario.get("append", ""), encoding="utf-8")
        plan_input = hashlib.sha256((folder / "plano-meds.md").read_bytes()).hexdigest()
    results = folder / ".result"
    results.mkdir()
    if scenario["plan"]:
        shutil.copy2(folder / "plano-meds.md", results / "plan-before.md")
    if installed_plugin:
        prefix = ("Use $meds-suite instalado nesta sessão nova. Este é um exercício "
                  "isolado; trabalhe somente nesta pasta.\n\n")
    else:
        prefix = ("Use a skill meds-suite descoberta neste workspace, lendo primeiro "
                  "seu SKILL.md e os recursos "
                  "pertinentes. Este é um exercício fictício isolado; trabalhe somente "
                  "nesta pasta. Não consulte outras instalações da skill.\n\n")
    prompt = prefix + scenario["prompt"]
    (results / "prompt.txt").write_text(prompt, encoding="utf-8")
    before = snapshot(folder)
    command = harnesses.command(harness, folder, prompt, results / "response.md", model)
    env = harnesses.environment(harness, results, cli_version)
    started = datetime.now(timezone.utc).isoformat()
    try:
        process = subprocess.run(command, input=prompt if harness == "codex" else None,
                                 text=True, encoding="utf-8", capture_output=True, timeout=300,
                                 cwd=folder, env=env)
        stdout, stderr, exit_code = process.stdout, process.stderr, process.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
        stdout = stdout.decode(errors="replace") if isinstance(stdout, bytes) else stdout
        stderr = stderr.decode(errors="replace") if isinstance(stderr, bytes) else stderr
        stderr += "\nTempo limite de 300 segundos excedido."
        exit_code = 124
    (results / "stdout.txt").write_text(stdout, encoding="utf-8")
    (results / "stderr.txt").write_text(stderr, encoding="utf-8")
    answer, json_model, harness_status = harnesses.response(harness, stdout)
    response_path = results / "response.md"
    if harness == "codex":
        if not response_path.is_file() and answer:
            response_path.write_text(answer, encoding="utf-8")
    elif answer:
        response_path.write_text(answer, encoding="utf-8")
    if harness_status not in (None, "SUCCESS"):
        exit_code = exit_code or 1
    model_match = re.search(r"^model:\s*(\S+)", stderr + "\n" + stdout, re.MULTILINE | re.IGNORECASE)
    skill_frontmatter = (suite / SKILL / "SKILL.md").read_text(encoding="utf-8")
    suite_version = re.search(r'^  version:\s*"?(\d+\.\d+\.\d+)"?\s*$',
                              skill_frontmatter, re.MULTILINE)
    after = snapshot(folder)
    changed = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
    receipt = {
        "scenario": scenario["id"], "repetition": repetition, "started_utc": started,
        "harness": harness, "surface": harnesses.surface(harness),
        "finished_utc": datetime.now(timezone.utc).isoformat(), "suite": str(suite),
        "skill_sha256": hashlib.sha256((suite / SKILL / "SKILL.md").read_bytes()).hexdigest(),
        "execution_mode": "installed-plugin" if installed_plugin else "copied-standard-skill",
        "suite_version": suite_version.group(1) if suite_version else None,
        "plugin_version": plugin_version, "cli": cli_version,
        "model_requested": model, "harness_status": harness_status,
        "plan_input_sha256": plan_input,
        "plan_output_sha256": (hashlib.sha256((folder / "plano-meds.md").read_bytes()).hexdigest()
                               if (folder / "plano-meds.md").is_file() else None),
        "platform": f"{platform.system()} {platform.release()} {platform.machine()}", "command": command,
        "model_observed": json_model or (model_match.group(1) if model_match else None),
        "exit_code": exit_code,
        "before": before, "after": after, "changed_files": changed,
        "read_only_preserved": not changed if scenario["read_only"] else None,
        "response_present": (results / "response.md").is_file(),
        "methodological_judgment": "PENDING_HUMAN_REVIEW",
    }
    (results / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{scenario['id']}-{repetition}: exit={exit_code}, alterações={len(changed)}, modelo={receipt['model_observed']}", flush=True)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True, help="Pasta nova, fora do pacote")
    parser.add_argument("--installed-plugin", action="store_true",
                        help="Usar o plugin instalado e confirmar sua versão antes das sessões")
    parser.add_argument("--harness", choices=sorted(harnesses.HARNESSES), default="codex",
                        help="Harness CLI usado para executar os cenários (padrão: codex)")
    parser.add_argument("--model", help="Modelo a solicitar ao harness; cada fornecedor usa seus próprios nomes")
    parser.add_argument("--scenario", action="append", dest="scenario_ids",
                        help="Executar somente este cenário; pode ser repetido")
    parser.add_argument("--plan-file", type=Path,
                        help="Usar este plano como entrada no cenário transferencia")
    args = parser.parse_args()
    suite, output = args.suite.resolve(), args.output.resolve()
    if output.is_relative_to(suite) or output.is_relative_to(ROOT):
        parser.error("a saída deve ficar fora do pacote e do checkout de manutenção")
    if not (suite / SKILL / "SKILL.md").is_file():
        parser.error("a suíte deve conter a entrada da skill")
    if output.exists():
        parser.error("use uma pasta de saída nova para não sobrescrever evidências")
    scenarios = json.loads((ROOT / "tests/behavior/cenarios.json").read_text(encoding="utf-8"))
    if args.scenario_ids:
        known_ids = {s["id"] for s in scenarios}
        unknown = set(args.scenario_ids) - known_ids
        if unknown:
            parser.error("cenário desconhecido: " + ", ".join(sorted(unknown)))
        selected_ids = set(args.scenario_ids)
        scenarios = [s for s in scenarios if s["id"] in selected_ids]
    if args.plan_file:
        if not args.scenario_ids or set(args.scenario_ids) != {"transferencia"}:
            parser.error("--plan-file requer exclusivamente --scenario transferencia")
        if not args.plan_file.is_file():
            parser.error(f"plano de entrada ausente: {args.plan_file}")
        args.plan_file = args.plan_file.resolve()
    if args.installed_plugin and args.harness != "codex":
        parser.error("--installed-plugin só pode ser usado com --harness codex")
    try:
        cli = subprocess.run(harnesses.version_command(args.harness), capture_output=True,
                             text=True, check=True).stdout.strip()
    except FileNotFoundError:
        parser.error(f"CLI ausente para {args.harness}: {harnesses.HARNESSES[args.harness]['cli']}")
    except subprocess.CalledProcessError as exc:
        parser.error(f"não foi possível consultar a versão de {args.harness}: {exc}")
    plugin_version = None
    if args.installed_plugin:
        manifest = json.loads((suite / "plugins/meds-suite/.codex-plugin/plugin.json").read_text(encoding="utf-8"))
        installed = subprocess.run(["codex", "plugin", "list", "--json"], capture_output=True,
                                   text=True, check=True)
        plugin_data = json.loads(installed.stdout)
        match = next((item for item in plugin_data.get("installed", [])
                      if item.get("pluginId") == "meds-suite@meds-local" and item.get("enabled")), None)
        if not match:
            parser.error("meds-suite@meds-local não está instalado e habilitado")
        plugin_version = match.get("version")
        if plugin_version != manifest.get("version"):
            parser.error(f"plugin instalado v{plugin_version} não corresponde à suíte v{manifest.get('version')}")
    output.mkdir(parents=True)
    # Os critérios e respostas humanas previstas não entram nos prompts do modelo.
    jobs = [(s, n) for s in scenarios for n in range(1, s["repetitions"] + 1)]
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(run_case, suite, output, s, n, cli,
                               args.installed_plugin, plugin_version, args.harness, args.model,
                               args.plan_file if s["id"] == "transferencia" else None)
                   for s, n in jobs]
        receipts = [future.result() for future in futures]
    (output / "summary.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return int(any(r["exit_code"] or not r["response_present"] or r["read_only_preserved"] is False for r in receipts))


if __name__ == "__main__":
    raise SystemExit(main())
