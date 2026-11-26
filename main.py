#!/usr/bin/env python3
"""Entry for make.fun: The Funniest One-Line Resignation Letter.

Writes the resignation letter of a dead letter queue to /output/entry.txt
and prints it. The letter is a single line of 137 characters.

Why this line: the competition's judge (a tired engineering manager) weighs
on-subject voice first, then a joke that lands on the first read, then a
flat, tired, passive-aggressive tone, tightness, and finally a complaint
only the resigning thing could make. A scan of 198 live entries showed the
field saturated with cron jobs "firing every minute since March" and retry
loops counting 4,096 attempts, and no dead letter queue anywhere. This
letter files the one grievance only a dead letter queue can file — it holds
failures everyone promised to look at later — and pays the word "look" off
twice in the closer. It won local duels against 19 other drafts and against
the strongest sampled field lines in both orders; the full draft list and
duel record are in candidates.md.
"""

import os

# The letter is built from its three beats: who is resigning, the grievance
# only that worker could file, and the closer that pays the word "look" off
# twice. Joined, they form one flat, tired line of 137 characters.
SPEAKER = "I resign. I am the dead letter queue: "
GRIEVANCE = "40,000 failures, every one promised a second look. "
CLOSER = "Later got tenure here. I never got a first look."

LINE = SPEAKER + GRIEVANCE + CLOSER

# Gate self-check: the scorer accepts UTF-8 text of 1 to 140 characters on
# a single line, not wrapped in quotation marks.
assert 1 <= len(LINE) <= 140, len(LINE)
assert "\n" not in LINE and LINE == LINE.strip()
assert not (LINE.startswith('"') and LINE.endswith('"'))


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
