#!/usr/bin/env python3
"""Gera ou verifica o espelho da Agent Skill no pacote Codex."""

import argparse
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("skills/meds-suite")
PACKAGE = Path("plugins/meds-suite/skills/meds-suite")
INTERFACE = Path("plugins/meds-suite/agents/openai.yaml")
PACKAGE_INTERFACE = PACKAGE / "agents/openai.yaml"


def files(base):
    return {path.relative_to(base).as_posix(): path.read_bytes()
            for path in sorted(base.rglob("*")) if path.is_file()}


def mismatches(root=ROOT):
    source = root / SOURCE
    package = root / PACKAGE
    expected = files(source)
    actual = files(package)
    actual.pop("agents/openai.yaml", None)
    errors = []
    for path in sorted(expected.keys() | actual.keys()):
        if expected.get(path) != actual.get(path):
            errors.append(path)
    interface = root / INTERFACE
    if not interface.is_file():
        errors.append(str(INTERFACE))
    if not (root / PACKAGE_INTERFACE).is_file():
        errors.append(str(PACKAGE_INTERFACE))
    return errors


def generate(root=ROOT):
    source = root / SOURCE
    destination = root / PACKAGE
    interface = root / INTERFACE
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        raise FileNotFoundError(f"fonte da skill ausente: {source}")
    if not interface.is_file():
        raise FileNotFoundError(f"metadados Codex ausentes: {interface}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as temporary:
        staging = Path(temporary) / destination.name
        shutil.copytree(source, staging)
        interface_target = staging / "agents/openai.yaml"
        interface_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(interface, interface_target)
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(staging), str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="falha se o pacote divergir da fonte")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()

    if args.check:
        errors = mismatches(root)
        for path in errors:
            print(f"DIVERGÊNCIA {path}")
        print(f"Espelho do pacote Codex: {'FALHA' if errors else 'OK'}")
        return int(bool(errors))

    generate(root)
    print("Pacote Codex gerado a partir de skills/meds-suite.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
