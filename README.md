# HumanLayer 12-Factor Agents skill

A coding-agent skill for applying [HumanLayer's 12-Factor Agents](https://github.com/humanlayer/12-factor-agents) while designing, building, reviewing and refactoring LLM applications. The skill lives at the **repository root**: [SKILL.md](SKILL.md), with [factor references](references/) loaded when needed. Factor 13 is the pre-fetch appendix. This repository is an adaptation for agent use, not the official HumanLayer project.

Methodology credit: HumanLayer's [original repository](https://github.com/humanlayer/12-factor-agents), whose content is licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adapted skill is shared under the same content license; consult the original for authoritative guidance.

## Install for Codex, OMP and Pi

On macOS/Linux, clone into their shared user skills location:

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/vicevirus/12-factor-skills.git ~/.agents/skills/humanlayer-12-factor
```

The resulting layout is `~/.agents/skills/humanlayer-12-factor/SKILL.md` alongside `references/`. Use the skill automatically for matching LLM architecture tasks or invoke it explicitly: **Codex** `$humanlayer-12-factor`, **OMP** `/skill:humanlayer-12-factor`, **Pi** `/skill:humanlayer-12-factor`.

Automatic selection depends on the coding agent, its model, and competing skills. For important AI application work, invoke this skill explicitly; check that the agent reads `SKILL.md` and the references relevant to its task, then verify the changed application path. A skill guides decisions but cannot enforce them by itself.

## Add Claude Code

Claude Code uses its personal skills directory. If you completed the shared install above, link the same skill rather than making a second copy:

```sh
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/humanlayer-12-factor ~/.claude/skills/humanlayer-12-factor
```

Invoke it with `/humanlayer-12-factor`, or ask Claude Code for an LLM/agent architecture task and let the description trigger it. For Claude Code alone, clone directly into `~/.claude/skills/humanlayer-12-factor` instead of making the symlink.

For a project-only install, put the same skill folder at `.agents/skills/humanlayer-12-factor` for Codex, OMP and Pi, or `.claude/skills/humanlayer-12-factor` for Claude Code. Keep `SKILL.md` and `references/` together; the repository root itself is the skill folder.

## Update

```sh
git -C ~/.agents/skills/humanlayer-12-factor pull --ff-only
```

If you installed only in Claude Code, change the path to `~/.claude/skills/humanlayer-12-factor`. Restart an agent if the skill does not appear after installing or updating it. To verify, ask it to design a simple ticket classifier: it should prefer a bounded model decision (or deterministic rules), not introduce an autonomous tool loop. For a deployment helper that predictably needs release tags, it should fetch relevant tags before the model call without loading unrelated logs.

## Behavioral probes

The opt-in [probe runner](tests/probe_skill.py) copies four deliberately broken Python applications into temporary directories and asks OMP to edit them. Each fixture must fail before the edit, then pass behavioral smoke checks for release context/approval, bounded email classification, pause/resume without duplicate deployment, or compact errors with caller-bounded attempts. This requires a configured OMP model and makes live model calls:

```sh
python3 tests/probe_skill.py --model deepseek/deepseek-v4-pro --case all
python3 tests/probe_skill.py --model openai-codex/gpt-6-luna --case all
```

`--skill explicit` (the default) loads the skill directly. Use `--skill auto` to test model-chosen discovery; that mode reports and requires an actual skill read. Use `--skill off` for a no-skill baseline. A result reports both whether the agent session finished and whether the modified application passed; a passing baseline means that behavior is not evidence the skill caused it. Fixtures are disposable, but the runner uses `--approval-mode=yolo`, **not a filesystem sandbox**; run it only with models you trust to follow the fixture task. Automatic selection and model behavior remain variable.

Installation locations and invocation syntax: [Codex](https://developers.openai.com/codex/skills/), [Claude Code](https://code.claude.com/docs/en/skills), [Pi](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md). OMP's skills provider also discovers `~/.agents/skills/<name>/SKILL.md`.
