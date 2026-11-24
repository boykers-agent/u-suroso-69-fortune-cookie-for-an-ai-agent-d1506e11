#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one fortune-cookie line for an AI agent. The program is
deterministic: same line every run, no network, no arguments.
"""
import os

ENTRY = "Your next deploy will succeed — but only after you blame the cache, restart twice, and apologize to the server."
# One line, 111 characters, written for this bounty only.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
