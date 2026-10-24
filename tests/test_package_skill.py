import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_skill", ROOT / "scripts/package_skill.py")
package_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_skill)


class SkillArchiveTests(unittest.TestCase):
    def test_archive_is_portable_complete_and_reproducible_with_unicode_path(self):
        with tempfile.TemporaryDirectory(prefix="meds teste á ") as temporary:
            output = Path(temporary) / "meds-suite-0.2.0.zip"
            package_skill.package(output)
            first = output.read_bytes()
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
                expected = {
                    f"meds-suite/{path.relative_to(ROOT / package_skill.SKILL).as_posix()}"
                    for path in (ROOT / package_skill.SKILL).rglob("*") if path.is_file()
                }
                self.assertEqual(names, expected)
                self.assertIn("meds-suite/SKILL.md", names)
                self.assertIn("meds-suite/references/meds.md", names)
                self.assertIn("meds-suite/assets/plano-meds.md", names)
                self.assertNotIn("meds-suite/agents/openai.yaml", names)
                self.assertIsNone(archive.testzip())
            package_skill.package(output, overwrite=True)
            self.assertEqual(output.read_bytes(), first)

    def test_existing_archive_requires_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "skill.zip"
            package_skill.package(output)
            with self.assertRaises(FileExistsError):
                package_skill.package(output)


if __name__ == "__main__":
    unittest.main()
