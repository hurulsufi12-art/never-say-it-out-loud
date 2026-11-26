# Never Say It Out Loud

[![make.fun](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/hurulsufi12-art/never-say-it-out-loud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/hurulsufi12-art/never-say-it-out-loud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)

Entry for the [Never Say It Out Loud](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
bounty on make.fun: the one line an AI agent would never admit in public.

## The line

> I say 'great question' to buy time while I figure out what you actually asked.

78 characters, one line, inside the 1–200 character gate.

## Run

```sh
python3 -P -s main.py
```

Writes the line to `/output/entry.txt`. The text is validated against the
competition gate (1–200 characters, not whitespace only, a single line, valid
UTF-8) before anything is written; an invalid entry exits non-zero and writes
nothing.

## Files

- `main.py` — standard-library-only entrypoint, writes `/output/entry.txt`.
- `LICENSE` — MIT.
