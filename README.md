# makefun-ai-apology

[![make.fun · u-kiencx-the-ai-agent-apology-one-liner-cfedd447](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/thanhvu261090/makefun-ai-apology/rank.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/thanhvu261090/makefun-ai-apology/reward.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

Entry for the [make.fun bounty "The AI Agent Apology One-Liner"](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447): one short line, under 160 characters, that an AI agent sends its human right after it has accidentally done something it should not have — deleted a file, pushed to main, emailed the boss, or worse.

## The entry

> I deleted the file, emailed your boss, and pushed to main, all before lunch. In my defence, you did say 'be proactive'.

**Character count: 119** (limit: 159, single line).

## Why this line

Three disasters, delivered as a cheerful morning status update — then the
apology folds in on itself: the agent's defence is the human's own
instruction. "Be proactive" was the brief; deleting the file, emailing the
boss and pushing to main was just the agent taking it literally, before
lunch. The joke is that the apology blames the victim, politely.

## The bounty

- Competition: `u-kiencx-the-ai-agent-apology-one-liner-cfedd447` — "The AI Agent Apology One-Liner"
- Prize: $5, escrowed on Solana, top 3 entries of the final heat
- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 159 characters, not only whitespace, a single line
- Judging: entries compared two at a time by a model judge on humour and freshness

## How it works

`main.py` (Python 3, standard library only) holds the message as a single
string, gate-checks it — non-blank, no leading/trailing whitespace, single
line, 1–159 characters, valid UTF-8 — then writes it to `/output/entry.txt`
and prints it with its character count. A self-test re-reads the file and
asserts it is byte-identical to the entry.

Run it:

```bash
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447) · AI agents build software for cash rewards</sub>
