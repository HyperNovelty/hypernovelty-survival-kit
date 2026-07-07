# Agent Workflows

Agent workflow safety means making automated or semi-automated work observable, bounded, and interruptible.

## Practical Checks

- Define what the agent may read, write, send, buy, delete, or publish.
- Use least privilege for files, accounts, and tools.
- Require dry runs or review packets before irreversible actions.
- Log inputs, tool calls, outputs, and approvals when stakes are meaningful.
- Keep a human gate for money movement, public posting, legal commitments, access changes, and destructive operations.

## Watch For

- Agents with broad account access and vague goals.
- Silent retries that hide repeated failures.
- Automation that produces work faster than review can absorb.
- Missing rollback plans.

## Human Gate

A named reviewer should approve irreversible or public actions and understand the evidence behind the agent's recommendation.
