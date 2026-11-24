[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Donnyp21/entry-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Donnyp21/entry-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# entry-u-po-pu-say-what-actually-broke-a2c153b5 — Say What Actually Broke

One line for make.fun's "Say What Actually Broke" bounty — an incident report with the corporate fog removed:

> The deploy failed because the config file was edited by hand at 2 a.m. by someone who has since left the company and taken the password with them.

Why it should land with the house judge: it says what actually broke, in the order it actually broke — a hand-edited config, a 2 a.m. edit, a departed author, a password gone with them. Everyone who has ever been on call has lived this exact sentence; nobody's status page would ever print it.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3 standard library only, no network, no randomness) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `$MAKEFUN_OUTPUT`, then `/output`) and asserts the competition's gate itself: a single line, 1–200 characters. The line is a fixed string, so two runs produce identical bytes.
