#!/usr/bin/env python3
"""One-line office joke for make.fun — The Funniest Office Joke, Judged Head to Head.

Writes the joke to /output/entry.txt (the sealed scorer's gate: UTF-8 text of
1 to 200 characters, not only white space) and prints it to stdout.
"""

import os

JOKE = "Our team-building day was cancelled for lack of teamwork, which honestly was the most team-building thing we've ever done."

def main():
    # Self-check: the sealed gate needs 1-200 UTF-8 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)

if __name__ == "__main__":
    main()
