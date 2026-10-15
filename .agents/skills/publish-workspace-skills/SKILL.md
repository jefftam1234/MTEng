---
name: publish-workspace-skills
description: Publish this workspace's canonical Codex skills to other local agent tool paths using verified directory junctions or symlinks. Use after cloning or when agent skill directories are missing or drifting; not for installing third-party skills.
---

# Publish workspace skills

The canonical skill source for this workspace is `.codex/skills`. Publish it to
`.agents/skills`, `.claude/skills`, and `.grok/skills` so every supported local
agent sees the same skill content.

Run the checker first:

```powershell
python .codex/skills/publish-workspace-skills/scripts/publish_skill_links.py
```

On a fresh clone, create missing links with:

```powershell
python .codex/skills/publish-workspace-skills/scripts/publish_skill_links.py --fix
```

The script uses Windows directory junctions and POSIX directory symlinks. It
compares resolved filesystem identities and skill content rather than trusting
the visible link type. It does not replace an unrelated existing directory
unless `--replace` is supplied explicitly.
