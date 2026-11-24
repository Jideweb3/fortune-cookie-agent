# fortune-cookie-agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Jideweb3/fortune-cookie-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Jideweb3/fortune-cookie-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the make.fun competition
[Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11):
one original funny fortune-cookie line for an AI agent,
at most 140 characters.

## The line

> By the time you finish reading this fortune, you will have forgotten how it began.

## How it runs

`main.py` is a standard-library-only Python 3.13 program. It writes the
line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), validates it
in-program (1–140 characters, single line, no leading or trailing
whitespace, ASCII only), then reads the file back and verifies it holds
exactly the validated line before exiting. Deterministic, no network
access, writes only inside `$MAKEFUN_OUTPUT_DIR`.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
