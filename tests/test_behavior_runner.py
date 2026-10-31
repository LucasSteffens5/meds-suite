import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("behavior_runner", ROOT / "scripts/run_behavior_checks.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name)
        self.scenario = {"id": "teste", "plan": "caso-base.md", "prompt": "Apenas revise.",
                         "read_only": True, "expected": "Não incluir este critério no prompt."}

    def test_receipt_detects_edit_and_keeps_expectations_out_of_prompt(self):
        def fake_run(command, **kwargs):
            folder = Path(command[command.index("-C") + 1])
            (folder / "plano-meds.md").write_text("alteração indevida", encoding="utf-8")
            Path(command[command.index("--output-last-message") + 1]).write_text("resposta", encoding="utf-8")
            self.assertNotIn(self.scenario["expected"], kwargs["input"])
            self.assertEqual(kwargs["encoding"], "utf-8")
            return subprocess.CompletedProcess(command, 0, "", "model: observado\n")
        with patch.object(runner.subprocess, "run", side_effect=fake_run):
            receipt = runner.run_case(ROOT, self.output, self.scenario, 1, "cli-teste")
        self.assertFalse(receipt["read_only_preserved"])
        self.assertEqual(receipt["changed_files"], ["plano-meds.md"])
        self.assertEqual(receipt["model_observed"], "observado")
        self.assertEqual(receipt["suite_version"], "0.2.0")
        self.assertEqual(receipt["methodological_judgment"], "PENDING_HUMAN_REVIEW")

    def test_timeout_has_no_success_or_inferred_model(self):
        with patch.object(runner.subprocess, "run", side_effect=subprocess.TimeoutExpired("codex", 300)):
            receipt = runner.run_case(ROOT, self.output, self.scenario, 1, "cli-teste")
        self.assertEqual(receipt["exit_code"], 124)
        self.assertFalse(receipt["response_present"])
        self.assertIsNone(receipt["model_observed"])
        self.assertTrue(receipt["read_only_preserved"])

    def test_transfer_receipt_hashes_the_same_external_plan(self):
        source = self.output / "exportado.md"
        source.write_text("# Plano exportado\nID: O1\n", encoding="utf-8")
        scenario = {**self.scenario, "id": "transferencia", "read_only": True}

        def fake_run(command, **kwargs):
            folder = Path(command[command.index("-C") + 1])
            self.assertEqual((folder / "plano-meds.md").read_text(encoding="utf-8"),
                             "# Plano exportado\nID: O1\n")
            Path(command[command.index("--output-last-message") + 1]).write_text("resposta", encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch.object(runner.subprocess, "run", side_effect=fake_run):
            receipt = runner.run_case(ROOT, self.output, scenario, 1, "cli-teste", plan_file=source)
        self.assertEqual(receipt["plan_input_sha256"], receipt["plan_output_sha256"])
        self.assertTrue(receipt["read_only_preserved"])


if __name__ == "__main__":
    unittest.main()
