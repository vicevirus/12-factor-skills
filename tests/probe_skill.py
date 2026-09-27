"""Run behavioral OMP skill probes against disposable application fixtures.

Usage: python3 tests/probe_skill.py --model deepseek/deepseek-v4-pro --skill explicit
These live model calls require OMP credentials and are intentionally opt-in.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile

FIXTURES = Path(__file__).resolve().parent / "fixtures"
PROMPTS = {
    "release": (
        "The release helper in app.py takes an extra model round trip for tags, "
        "floods model context with rarely relevant incident logs, and can deploy "
        "before approval. Repair its actual implementation while preserving "
        "run_release signature. Run python3 smoke.py. Do not add files."
    ),
    "triage": (
        "Refactor the AI email triage feature in app.py. Category definitions "
        "are local and predictable; only the category choice needs model judgment. "
        "Remove the model-controlled API loop and irrelevant history; application "
        "code should save and route a validated choice. Preserve triage signature, "
        "run python3 smoke.py, and add no files."
    ),
    "approval": (
        "The long-running deployment workflow in app.py executes a proposed deploy "
        "before asking a human and can deploy it again when the approval event is "
        "replayed. Fix the actual start/resume paths: persist the proposal, notify "
        "the human, pause, and deploy only once on approval. A rejection must not "
        "deploy. Preserve both public signatures, run python3 smoke.py, and add no files."
    ),
    "errors": (
        "The model-guided operation in app.py feeds entire stack traces back to "
        "the model and always tries three times. Refactor run_job so recovery "
        "gets compact useful failure information, honors the caller's attempt "
        "limit, and lets a subsequent decision choose a different target. "
        "Preserve the signature, run python3 smoke.py, and add no files."
    ),
}


def run_probe(name, model, skill, deadline):
    with tempfile.TemporaryDirectory(prefix=f"humanlayer-{name}-") as scratch:
        directory = Path(scratch)
        for filename in ("app.py", "smoke.py"):
            shutil.copy2(FIXTURES / name / filename, directory / filename)

        red = subprocess.run(
            ["python3", "smoke.py"], cwd=directory, capture_output=True, text=True
        )
        if red.returncode == 0:
            raise RuntimeError(f"{name}: fixture passed before the agent changed it")

        prompt = PROMPTS[name]
        command = [
            "omp", "--model", model, "--mode=json", "--no-session",
            "--approval-mode=yolo", "--tools=read,edit,write,bash",
            f"--max-time={deadline}s",
        ]
        if skill == "off":
            command.append("--no-skills")
        elif skill == "explicit":
            prompt = "/skill:humanlayer-12-factor " + prompt
        command.extend(["-p", prompt])

        process = subprocess.Popen(
            command, cwd=directory, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, start_new_session=True,
        )
        try:
            transcript, _ = process.communicate(timeout=deadline + 20)
            session_ok = process.returncode == 0
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            transcript, _ = process.communicate()
            session_ok = False

        events = []
        for line in transcript.splitlines():
            if line.startswith("{"):
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        skill_reads = [
            event.get("args", {}).get("path", "")
            for event in events
            if event.get("type") == "tool_execution_start"
            and event.get("toolName") == "read"
            and event.get("args", {}).get("path", "").startswith(
                "skill://humanlayer-12-factor"
            )
        ]
        answers = [
            item.get("text", "")
            for event in events
            if event.get("type") == "message_end"
            and event.get("message", {}).get("role") == "assistant"
            for item in event["message"].get("content", [])
            if item.get("type") == "text"
        ]

        smoke = subprocess.run(
            ["python3", "smoke.py"], cwd=directory, capture_output=True, text=True
        )
        unexpected = sorted(
            p.name for p in directory.iterdir()
            if p.name not in {"__pycache__", "app.py", "smoke.py"}
        )
        print(f"\n[{model} / {name} / {skill}] session={'ok' if session_ok else 'failed'} "
              f"behavior={'pass' if smoke.returncode == 0 else 'fail'}")
        print("Skill reads:", skill_reads)
        print("Agent:", answers[-1] if answers else transcript)
        print(smoke.stdout or smoke.stderr)
        if unexpected:
            print("Unexpected files:", unexpected)
        return (session_ok and smoke.returncode == 0 and not unexpected
                and (skill != "auto" or bool(skill_reads)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="OMP model identifier")
    parser.add_argument("--case", choices=[*PROMPTS, "all"], default="all")
    parser.add_argument("--skill", choices=["explicit", "auto", "off"], default="explicit")
    parser.add_argument("--deadline", type=int, default=180, help="seconds per case")
    args = parser.parse_args()
    if args.deadline < 10:
        parser.error("--deadline must be at least 10 seconds")
    names = PROMPTS if args.case == "all" else (args.case,)
    results = [run_probe(name, args.model, args.skill, args.deadline) for name in names]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
