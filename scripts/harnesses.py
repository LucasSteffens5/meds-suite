"""Adaptadores de linha de comando para os seis harnesses da matriz."""

import json
import os
import re
import shutil
from pathlib import Path


SKILL = Path("skills/meds-suite")
HARNESSES = {
    "codex": {"cli": "codex", "skills": Path(".agents/skills/meds-suite"),
              "surface": "Codex CLI"},
    "claude-code": {"cli": "claude", "skills": Path(".claude/skills/meds-suite"),
                    "surface": "Claude Code CLI"},
    "antigravity": {"cli": "agy", "skills": Path(".agents/skills/meds-suite"),
                    "surface": "Antigravity CLI"},
    "opencode": {"cli": "opencode", "skills": Path(".agents/skills/meds-suite"),
                 "surface": "OpenCode CLI"},
    "cursor": {"cli": ("agent", "cursor-agent"), "skills": Path(".agents/skills/meds-suite"),
               "surface": "Cursor CLI"},
    "github-copilot": {"cli": "copilot", "skills": Path(".agents/skills/meds-suite"),
                       "surface": "GitHub Copilot CLI"},
}


def executable(harness):
    candidates = HARNESSES[harness]["cli"]
    if isinstance(candidates, str):
        candidates = (candidates,)
    return next((shutil.which(candidate) for candidate in candidates
                 if shutil.which(candidate)), candidates[0])


def install_skill(suite, folder, harness, installed_plugin=False):
    if installed_plugin:
        return None
    destination = folder / HARNESSES[harness]["skills"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(suite / SKILL, destination)
    return destination


def command(harness, folder, prompt, response_path, model=None):
    """Build a non-interactive command with file access bounded to the case."""
    cli = executable(harness)
    if harness == "codex":
        result = [cli, "exec", "--ephemeral", "--sandbox", "workspace-write",
                  "--skip-git-repo-check", "-C", str(folder), "--color", "never",
                  "--output-last-message", str(response_path)]
        if model:
            result.extend(["--model", model])
        return result + ["-"]
    if harness == "claude-code":
        result = [cli, "-p", prompt, "--output-format", "text", "--permission-mode", "dontAsk",
                  "--tools", "Read,Write,Edit,Glob,Grep",
                  "--allowedTools", "Read", "Write", "Edit", "Glob", "Grep",
                  "--disallowedTools", "Bash"]
        if model:
            result.extend(["--model", model])
        return result
    if harness == "antigravity":
        result = [cli, "-p", prompt, "--output-format", "json", "--sandbox"]
        if model:
            result.extend(["--model", model])
        return result
    if harness == "opencode":
        result = [cli, "run", "--dir", str(folder)]
        if model:
            result.extend(["--model", model])
        return result + [prompt]
    if harness == "cursor":
        result = [cli, "-p", "--force", "--sandbox", "enabled", "--output-format", "text"]
        if model:
            result.extend(["--model", model])
        return result + [prompt]
    if harness == "github-copilot":
        result = [cli, "-p", prompt, "--silent", "--no-ask-user",
                  "--available-tools=view,create,edit,grep,glob,skill",
                  "--allow-tool=read,write", "--deny-tool=shell,url,memory"]
        if model:
            result.extend(["--model", model])
        return result
    raise ValueError(f"harness desconhecido: {harness}")


def environment(harness, results, cli_version=None):
    """Return per-process overrides for isolated and restricted runner settings."""
    if harness != "opencode":
        return None
    match = re.search(r"(?<!\d)(\d+)\.\d+\.\d+", cli_version or "")
    if not match:
        raise ValueError("versão do OpenCode não reconhecida; não é seguro escolher o esquema de permissões")
    major = int(match.group(1))
    if major == 1:
        config = {
            "permission": {
                "*": "deny", "read": "allow", "edit": "allow", "list": "allow",
                "glob": "allow", "grep": "allow", "skill": "allow",
                "external_directory": "deny", "bash": "deny", "task": "deny",
                "webfetch": "deny", "websearch": "deny", "question": "deny",
            },
        }
    elif major >= 2:
        config = {
            "permissions": [
                {"action": "*", "resource": "*", "effect": "deny"},
                {"action": "read", "resource": "*", "effect": "allow"},
                {"action": "edit", "resource": "*", "effect": "allow"},
                {"action": "glob", "resource": "*", "effect": "allow"},
                {"action": "grep", "resource": "*", "effect": "allow"},
                {"action": "skill", "resource": "*", "effect": "allow"},
                {"action": "external_directory", "resource": "*", "effect": "deny"},
                {"action": "shell", "resource": "*", "effect": "deny"},
            ],
        }
    else:
        raise ValueError(f"OpenCode v{major} não é suportado pelo adaptador de permissões")
    env = os.environ.copy()
    env["OPENCODE_CONFIG_CONTENT"] = json.dumps(config)
    return env


def response(harness, stdout):
    """Extract the answer text and an observed model when the CLI reports one."""
    if harness == "antigravity":
        try:
            result = json.loads(stdout)
        except json.JSONDecodeError:
            return stdout, None, "invalid-json"
        status = result.get("status")
        return result.get("response", ""), result.get("model"), status
    return stdout, None, None


def version_command(harness):
    return [executable(harness), "--version"]


def surface(harness):
    return HARNESSES[harness]["surface"]
