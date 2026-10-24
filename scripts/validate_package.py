#!/usr/bin/env python3
"""Verifica estrutura e portabilidade do pacote, sem alterar arquivos."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


PLUGIN = Path("plugins/meds-suite")
SKILL = Path("skills/meds-suite")
PACKAGE_SKILL = PLUGIN / "skills/meds-suite"
LEGEND = (
    "**Legenda:** ID = identificador; O = objetivo da avaliação; P = propriedade do artefato; "
    "E = episódio de avaliação; S = cenário; D = documento. Os números identificam itens, "
    "não passos de MEDS.\n\n"
    "**Siglas:** MEDS = metodologia para organizar avaliações em DSR; DSR = pesquisa em "
    "ciência do design; DSRM = metodologia do projeto DSR; FEDS = estratégia e trajetória "
    "das avaliações; DSREMSF = seleção de métodos de avaliação; MuSCoW = prioridades: "
    "Must (precisa), Should (deveria), Could (poderia), Would (seria desejável avaliar)."
)
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
    if (not frontmatter or not re.search(r"^name: meds-suite\s*$", header, re.MULTILINE)
            or not re.search(r"^description:\s*\S.+$", header, re.MULTILINE)):
        error(skill_path, "frontmatter/name/description ausente ou inválido")
    versions = re.findall(r'^  version: "(\d+\.\d+\.\d+)"\s*$', header, re.MULTILINE)
    readme = read(Path("README.md"))
    readme_versions = re.findall(r"^MEDS Suite (\d+\.\d+\.\d+) oferece\b", readme, re.MULTILINE)
    version = manifest.get("version")
    if (not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version)
            or versions != [version] or readme_versions != [version]):
        error(manifest_path, "versões do plugin, skill e apresentação no README devem coincidir")
    if skill_text.count(LEGEND) != 1:
        error(skill_path, "deve conter uma única legenda fixa para as respostas da suíte")
    if re.search(r"tutorial|ensinar MEDS|exemplo simples", header, re.IGNORECASE):
        error(skill_path, "descrição da skill não deve promover um tutorial como modo de uso")
    interface_path = PLUGIN / "agents/openai.yaml"
    interface = read(interface_path)
    if re.search(r"tutorial|ensinar MEDS|exemplo simples", interface, re.IGNORECASE):
        error(interface_path, "metadados de interface não devem promover um tutorial como modo de uso")

    skills = sorted(path.relative_to(root).as_posix() for path in root.rglob("SKILL.md")
                    if ".git" not in path.parts and "__pycache__" not in path.parts)
    expected_skills = [(SKILL / "SKILL.md").as_posix(),
                       (PACKAGE_SKILL / "SKILL.md").as_posix()]
    if skills != sorted(expected_skills):
        error(SKILL, "deve haver uma fonte comum e somente seu espelho no pacote Codex")

    source_files = {
        path.relative_to(root / SKILL).as_posix(): path.read_bytes()
        for path in sorted((root / SKILL).rglob("*")) if path.is_file()
    }
    package_files = {
        path.relative_to(root / PACKAGE_SKILL).as_posix(): path.read_bytes()
        for path in sorted((root / PACKAGE_SKILL).rglob("*")) if path.is_file()
        and path.relative_to(root / PACKAGE_SKILL).as_posix() != "agents/openai.yaml"
    }
    if source_files != package_files:
        error(PACKAGE_SKILL, "espelho Codex diverge da fonte comum; execute scripts/sync_codex_package.py")
    interface_source = root / interface_path
    interface_package = root / PACKAGE_SKILL / "agents/openai.yaml"
    if not interface_package.is_file() or (interface_source.is_file()
                                           and interface_package.read_bytes() != interface_source.read_bytes()):
        error(interface_package.relative_to(root), "metadados Codex ausentes ou divergentes da fonte do pacote")
    if (root / SKILL / "agents/openai.yaml").exists():
        error(SKILL, "metadados de interface devem existir somente no pacote Codex")
    tutorial_dir = root / SKILL / "workflows/tutorial"
    if tutorial_dir.exists():
        error(tutorial_dir.relative_to(root), "tutoriais devem permanecer fora do plugin instalado")
    tutorial_markers = (
        "casos/tutorial-meds/",
        "D1 é “Calendário acadêmico”",
        "D2 é “Guia de matrícula”",
        "D3 é “Modelo de relatório”",
    )
    for path in sorted((root / SKILL).rglob("*.md")):
        content = read(path.relative_to(root))
        if re.search(r"codex|claude|antigravity|opencode|cursor|copilot", content, re.IGNORECASE):
            error(path.relative_to(root), "a fonte comum não deve depender de um harness específico")
        for marker in tutorial_markers:
            if marker in content:
                error(path.relative_to(root), "dados do tutorial não podem entrar no plugin instalado")
                break
    for required in ("workflows/planejar/WORKFLOW.md",
                     "workflows/revisar/WORKFLOW.md", "references/meds.md",
                     "references/feds.md", "references/dsrm.md", "assets/plano-meds.md"):
        if not (root / SKILL / required).is_file():
            error(SKILL / required, "recurso obrigatório ausente")

    resources = [root / "README.md", root / "docs/primeiro-contato/README.md",
                 *sorted((root / SKILL).rglob("*.md")),
                 *sorted((root / PACKAGE_SKILL).rglob("*.md"))]
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
            package_root = (root / (PACKAGE_SKILL if relative.is_relative_to(PACKAGE_SKILL)
                                    else SKILL)).resolve()
            if ((relative.is_relative_to(SKILL) or relative.is_relative_to(PACKAGE_SKILL))
                    and not destination.is_relative_to(package_root)):
                error(relative, f"link local depende de arquivo fora da skill instalada: {target}")
            if not destination.is_relative_to(root) or not destination.exists():
                error(relative, f"link local ausente ou fora do pacote: {target}")

    template_path = SKILL / "assets/plano-meds.md"
    template = read(template_path)
    if template.count("## Legenda") != 1 or template.count(LEGEND) != 1 or not template.rstrip().endswith(LEGEND):
        error(template_path, "deve terminar com uma única cópia da legenda fixa")
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
