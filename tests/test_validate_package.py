import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_package", ROOT / "scripts/validate_package.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("plugins", ".agents", "tests/behavior"):
            shutil.copytree(ROOT / directory, self.root / directory)
        tutorial_doc = self.root / "docs/primeiro-contato"
        tutorial_doc.mkdir(parents=True)
        shutil.copy2(ROOT / "docs/primeiro-contato/README.md", tutorial_doc / "README.md")
        for filename in ("README.md", "LICENSE"):
            shutil.copy2(ROOT / filename, self.root / filename)

    def change_manifest(self, value, marketplace=False):
        path = (Path(".agents/plugins/marketplace.json") if marketplace
                else validator.PLUGIN / ".codex-plugin/plugin.json")
        (self.root / path).write_text(json.dumps(value), encoding="utf-8")

    def test_current_package_and_read_only(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(validator.validate(self.root), [])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_invalid_manifest_shapes_and_json(self):
        path = self.root / validator.PLUGIN / ".codex-plugin/plugin.json"
        for value in ("[", "null", "[]", '{"skills": 42}'):
            with self.subTest(value=value):
                path.write_text(value, encoding="utf-8")
                self.assertTrue(validator.validate(self.root))

    def test_missing_and_external_declared_paths(self):
        path = self.root / validator.PLUGIN / ".codex-plugin/plugin.json"
        original = json.loads(path.read_text())
        for target in ("./missing", "../../../", "https://example.org", ""):
            with self.subTest(target=target):
                self.change_manifest(dict(original, skills=target))
                self.assertTrue(validator.validate(self.root))

    def test_invalid_marketplace_entries(self):
        for entries in (None, [], [None], [{"name": "meds-suite", "source": None}]):
            with self.subTest(entries=entries):
                self.change_manifest({"name": "meds-local", "plugins": entries}, marketplace=True)
                self.assertTrue(validator.validate(self.root))

    def test_version_drift_in_each_surface(self):
        paths = [validator.PLUGIN / ".codex-plugin/plugin.json", validator.SKILL / "SKILL.md", Path("README.md")]
        for path in paths:
            with self.subTest(path=path):
                file = self.root / path
                original = file.read_text()
                file.write_text(original.replace("0.1.3", "9.9.9"), encoding="utf-8")
                self.assertTrue(validator.validate(self.root))
                file.write_text(original, encoding="utf-8")

    def test_duplicate_skill_and_missing_workflow(self):
        tutorial = self.root / validator.SKILL / "workflows/tutorial/WORKFLOW.md"
        content = tutorial.read_text(encoding="utf-8")
        tutorial.unlink()
        self.assertTrue(any("tutorial" in e for e in validator.validate(self.root)))
        tutorial.write_text(content, encoding="utf-8")
        extra = self.root / validator.SKILL / "workflows/planejar/SKILL.md"
        extra.write_text("extra", encoding="utf-8")
        self.assertTrue(validator.validate(self.root))
        extra.unlink()
        (extra.parent / "WORKFLOW.md").unlink()
        self.assertTrue(validator.validate(self.root))

    def test_broken_relative_link_reference_and_unicode(self):
        path = self.root / validator.SKILL / "references/meds.md"
        original = path.read_text()
        for link in ("[ausente](ausente.md)", "[x][alvo]\n[alvo]: ausente.md", "[fora](../../../../../fora.md)"):
            with self.subTest(link=link):
                path.write_text(original + "\n" + link, encoding="utf-8")
                self.assertTrue(validator.validate(self.root))
        target = path.parent / "arquivo com acento á.md"
        target.write_text("ok", encoding="utf-8")
        path.write_text(original + "\n[x](arquivo%20com%20acento%20%C3%A1.md)", encoding="utf-8")
        self.assertEqual(validator.validate(self.root), [])

    def test_plugin_resources_cannot_depend_on_checkout_docs(self):
        tutorial = self.root / validator.SKILL / "workflows/tutorial/WORKFLOW.md"
        original = tutorial.read_text(encoding="utf-8")
        tutorial.write_text(original + "\n[material externo](../../../../../../docs/primeiro-contato/README.md)\n",
                            encoding="utf-8")
        self.assertTrue(any("fora do plugin instalado" in e
                            for e in validator.validate(self.root)))

    def test_exported_template_rejects_even_existing_install_link(self):
        path = self.root / validator.SKILL / "assets/plano-meds.md"
        path.write_text(path.read_text() + "\n[FEDS](../references/feds.md)", encoding="utf-8")
        self.assertTrue(any("modelo exportável" in e for e in validator.validate(self.root)))

    def test_legend_must_be_unique_and_final_in_deliverables(self):
        for relative in (validator.SKILL / "assets/plano-meds.md",):
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_text(encoding="utf-8")
                path.write_text(original + "\n\n## Nota após a legenda\n", encoding="utf-8")
                self.assertTrue(any("legenda fixa" in e for e in validator.validate(self.root)))
                path.write_text(original, encoding="utf-8")

    def test_exported_template_rejects_install_path_in_prose(self):
        path = self.root / validator.SKILL / "assets/plano-meds.md"
        path.write_text(path.read_text() + "\nConsultar `/Users/exemplo/.codex/skills/meds-suite`.", encoding="utf-8")
        self.assertTrue(any("caminho da instalação" in e for e in validator.validate(self.root)))

    def test_file_url_and_malformed_url_are_reported(self):
        path = self.root / validator.SKILL / "assets/plano-meds.md"
        original = path.read_text()
        for link in ("[local](file:///tmp/feds.md)", "[inválido](https://[)"):
            with self.subTest(link=link):
                path.write_text(original + "\n" + link, encoding="utf-8")
                self.assertTrue(validator.validate(self.root))

    def test_unreadable_resource_and_cli_exit_codes(self):
        command = [sys.executable, str(ROOT / "scripts/validate_package.py"), "--root", str(self.root)]
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        (self.root / validator.SKILL / "references/feds.md").write_bytes(b"\xff")
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("references/feds.md", result.stdout)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
