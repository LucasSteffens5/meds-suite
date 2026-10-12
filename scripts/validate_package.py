#!/usr/bin/env python3
"""Verifica estrutura e portabilidade do pacote, sem alterar arquivos."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


PLUGIN = Path("plugins/meds-suite")
SKILL = PLUGIN / "skills/meds-suite"
# shortcut: cobre links inline e definições de referência usados neste pacote;
# adotar um parser Markdown se os recursos passarem a usar sintaxe mais complexa.
LINKS = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\s*\)")
DEFINITIONS = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)


def link_targets(text):
    return [match.group(1).strip("<>") for pattern in (LINKS, DEFINITIONS)
            for match in pattern.finditer(text)]


def validate(root):
    root = Path(root).resolve()
    errors = []

    def error(path, message):
        errors.append(f"{path}: {message}")

    def read(path):
        try:
            return (root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            error(path, f"não foi possível ler: {exc}")
            return ""

    def document(path):
        try:
            value = json.loads(read(path))
        except json.JSONDecodeError as exc:
            error(path, f"JSON inválido na linha {exc.lineno}")
            return {}
        if not isinstance(value, dict):
            error(path, "o JSON deve ser um objeto")
            return {}
        return value

    def directory(base, value, expected, owner):
        if not isinstance(value, str) or not value:
            error(owner, "caminho local ausente ou inválido")
            return
        try:
            scheme = urlsplit(value).scheme
        except ValueError:
            error(owner, "caminho local inválido")
            return
        if scheme:
            error(owner, "caminho deve ser local")
            return
        target = (root / base / value).resolve()
        if target != (root / expected).resolve() or not target.is_dir():
            error(owner, f"caminho deve resolver para {expected}, diretório existente")

    marketplace_path = Path(".agents/plugins/marketplace.json")
    marketplace = document(marketplace_path)
    if marketplace.get("name") != "meds-local":
        error(marketplace_path, "nome esperado: meds-local")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        error(marketplace_path, "deve declarar exatamente um plugin")
    else:
        entry = entries[0]
        if entry.get("name") != "meds-suite":
            error(marketplace_path, "plugin esperado: meds-suite")
        source = entry.get("source")
        if not isinstance(source, dict) or source.get("source") != "local":
            error(marketplace_path, "source deve declarar uma origem local")
        else:
            directory(Path(), source.get("path"), PLUGIN, marketplace_path)

    manifest_path = PLUGIN / ".codex-plugin/plugin.json"
    manifest = document(manifest_path)
    if manifest.get("name") != "meds-suite":
        error(manifest_path, "nome esperado: meds-suite")
    directory(PLUGIN, manifest.get("skills"), PLUGIN / "skills", manifest_path)

    skill_path = SKILL / "SKILL.md"
    skill_text = read(skill_path)
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", skill_text, re.DOTALL)
    header = frontmatter.group(1) if frontmatter else ""
    if not frontmatter or not re.search(r"^name: meds-suite\s*$", header, re.MULTILINE):
        error(skill_path, "frontmatter/name ausente ou inválido")
    versions = re.findall(r'^  version: "(\d+\.\d+\.\d+)"\s*$', header, re.MULTILINE)
    readme = read(Path("README.md"))
    readme_versions = re.findall(r"^Plugin `meds-suite` v(\d+\.\d+\.\d+)\b", readme, re.MULTILINE)
    version = manifest.get("version")
    if (not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version)
            or versions != [version] or readme_versions != [version]):
        error(manifest_path, "versões do plugin, skill e apresentação no README devem coincidir")

    skills = sorted((root / "plugins").rglob("SKILL.md"))
    if skills != [root / skill_path]:
        error(PLUGIN, "deve existir somente a entrada skills/meds-suite/SKILL.md")
    for required in ("agents/openai.yaml", "workflows/planejar/WORKFLOW.md",
                     "workflows/revisar/WORKFLOW.md", "references/meds.md",
                     "references/feds.md", "references/dsrm.md", "assets/plano-meds.md"):
        if not (root / SKILL / required).is_file():
            error(SKILL / required, "recurso obrigatório ausente")

    resources = [root / "README.md", *sorted((root / SKILL).rglob("*.md"))]
    for path in resources:
        relative = path.relative_to(root)
        for target in link_targets(read(relative)):
            try:
                url = urlsplit(target)
            except ValueError:
                error(relative, f"link malformado: {target}")
                continue
            if (url.scheme and url.scheme != "file") or url.netloc or not url.path:
                continue
            destination = (path.parent / unquote(url.path)).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                error(relative, f"link local ausente ou fora do pacote: {target}")

    template_path = SKILL / "assets/plano-meds.md"
    template = read(template_path)
    for target in link_targets(template):
        try:
            url = urlsplit(target)
        except ValueError:
            error(template_path, f"link malformado: {target}")
            continue
        if url.scheme == "file" or (not url.scheme and not url.netloc and url.path):
            error(template_path, f"modelo exportável contém link dependente de local: {target}")
    if re.search(r"/Users/|/home/|CODEX_HOME|\.codex/|plugins/meds-suite/|references/\S+\.md", template):
        error(template_path, "modelo exportável contém caminho da instalação")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f"FALHA {error}")
    print(f"Estrutura do pacote: {'FALHA' if errors else 'OK'}; não avalia correção metodológica.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
