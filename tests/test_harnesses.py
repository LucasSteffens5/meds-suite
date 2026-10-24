import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("harnesses", ROOT / "scripts/harnesses.py")
harnesses = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harnesses)


class HarnessTests(unittest.TestCase):
    def test_all_six_harnesses_have_commands_and_scoped_skill_locations(self):
        self.assertEqual(set(harnesses.HARNESSES), {
            "codex", "claude-code", "antigravity", "opencode", "cursor", "github-copilot"
        })
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            for harness in harnesses.HARNESSES:
                with self.subTest(harness=harness):
                    command = harnesses.command(harness, folder, "prompt", folder / "response.md")
                    self.assertTrue(command)
                    self.assertTrue(str(harnesses.HARNESSES[harness]["skills"]).endswith("meds-suite"))

    def test_command_permissions_block_unneeded_shell_access(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            claude = harnesses.command("claude-code", folder, "prompt", folder / "response.md")
            self.assertIn("dontAsk", claude)
            self.assertIn("--disallowedTools", claude)
            self.assertIn("Bash", claude)
            self.assertIn("Read,Write,Edit,Glob,Grep", claude)
            self.assertEqual(claude[claude.index("--allowedTools") + 1:
                                    claude.index("--disallowedTools")],
                             ["Read", "Write", "Edit", "Glob", "Grep"])

            copilot = harnesses.command("github-copilot", folder, "prompt", folder / "response.md")
            self.assertIn("--deny-tool=shell,url,memory", copilot)
            self.assertIn("--available-tools=view,create,edit,grep,glob,skill", copilot)

            config_v1 = json.loads(harnesses.environment("opencode", folder, "1.0.0")["OPENCODE_CONFIG_CONTENT"])
            self.assertEqual(config_v1["permission"]["bash"], "deny")
            config_v2 = json.loads(harnesses.environment("opencode", folder, "OpenCode 2.0.1")["OPENCODE_CONFIG_CONTENT"])
            self.assertEqual(config_v2["permissions"][0],
                             {"action": "*", "resource": "*", "effect": "deny"})
            self.assertEqual(config_v2["permissions"][-1]["action"], "shell")

            antigravity = harnesses.command("antigravity", folder, "prompt", folder / "response.md")
            self.assertIn("--sandbox", antigravity)
            cursor = harnesses.command("cursor", folder, "prompt", folder / "response.md")
            self.assertIn("enabled", cursor)

    def test_skill_copy_uses_each_harness_discovery_path(self):
        with tempfile.TemporaryDirectory(prefix="caminho com espaço á ") as temporary:
            root = Path(temporary)
            source = root / "suite/skills/meds-suite"
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text("skill", encoding="utf-8")
            for harness, data in harnesses.HARNESSES.items():
                with self.subTest(harness=harness):
                    workspace = root / harness
                    workspace.mkdir()
                    destination = harnesses.install_skill(root / "suite", workspace, harness)
                    self.assertEqual(destination, workspace / data["skills"])
                    self.assertEqual((destination / "SKILL.md").read_text(), "skill")

    def test_antigravity_json_status_and_answer_are_preserved(self):
        answer, model, status = harnesses.response(
            "antigravity", '{"status":"SUCCESS","response":"ok","model":"test-model"}'
        )
        self.assertEqual((answer, model, status), ("ok", "test-model", "SUCCESS"))


if __name__ == "__main__":
    unittest.main()
