# Installation guide (v1.0)

Committing SKILL.md on GitHub is **not the same as activating it** in any assistant account. This is a portable instruction package, not a broker, plugin, or independently-running agent.

Repository: Maximumz1/MathModelAgent-Research, research-skills/asset-management-research on branch chatgpt-research-adaptation (after approved PR merge). During review it is on feature/asset-management-research-v1-20261021.

Codex (where project-local skills are supported): copy the complete folder into .agents/skills/asset-management-research in a Codex project; check the version-specific skill discovery procedure and restart/reload if necessary.

Claude Code (where project-local skills are supported): copy the folder into .claude/skills/asset-management-research and reopen/reload. Preserve references and optional audit script.

ChatGPT: explicitly refer to the GitHub SKILL.md path in the Investment Project instructions and use a connected GitHub source or upload the ZIP. GitHub commit alone does not install a native ChatGPT Skill; executing Python requires a supported code environment.

Do not automatically install AssetManagementToolkit. Review its licensing and only separately install as an explicit user-approved external Python dependency. The Skill does not distribute external toolkit code.

Suggested Project instruction: "For portfolio quantitative analysis, consult the Asset Management Research Skill v1.0 in Maximumz1/MathModelAgent-Research, research-skills/asset-management-research/SKILL.md; use current Investment Project sources for numerical truth; preserve CSV/JSON/ZIP; do not execute trades or claim historical outperformance is predictive."
