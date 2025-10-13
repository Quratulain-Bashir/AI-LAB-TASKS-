# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# LAB TASK 4 — Utilities CLI

Overview
- Small command-line tool providing three utilities:
  1. Luhn credit-card number validator
  2. Remove ASCII punctuation from text
  3. Sort words in a sentence (alphabetical, case-insensitive)

Files
- `LAB TASK 4.PY` — main script containing all logic and a text menu.
- `README.md` — this file (explanation and usage).

How it works (brief)
- The script presents a simple interactive menu (choices 1–4).
- User selects an option and follows prompts. Enter `4` or type `q`, `quit`, or `exit` to quit.

Key functions
- luhn_valid(card_number: str) -> bool
  - Strips non-digits, applies the Luhn algorithm, and returns True if the number is valid.
  - Useful for basic credit-card number validation (accepts spaces/dashes).
- remove_punctuation(text: str) -> str
  - Removes ASCII punctuation characters using str.translate() and returns the cleaned text.
- sort_sentence(sentence: str) -> str
  - Splits a sentence into words, sorts them case-insensitively, and returns them joined by single spaces.
- prompt(msg: str) -> str
  - Wrapper around input() that exits gracefully on EOF/KeyboardInterrupt.
- menu() -> None
  - Main interactive loop: displays options, reads user input, calls utilities, prints results.

Usage
1. Open a terminal (PowerShell / CMD) on Windows.
2. Run:
   python "LAB TASK 4.PY"
3. Choose an option:
   - 1: Enter a card number (digits, spaces, dashes allowed) → prints "Valid" or "Invalid".
   - 2: Paste/enter text → prints text without punctuation.
   - 3: Enter a sentence → prints words sorted alphabetically.
   - 4 / q / quit / exit → exit.

Example session
- Select 1 → Enter `4539 1488 0343 6467` → Output: `Valid`
- Select 2 → Enter `Hello, world!` → Output: `Hello world`
- Select 3 → Enter `banana Apple cherry` → Output: `Apple banana cherry`

Notes & Extensions
- Luhn check is syntactic only — it does not verify issuer/account existence.
- remove_punctuation removes ASCII punctuation only; non-ASCII punctuation remains.
- Extensions: add per-option help, file input/output, support for non-ASCII normalization, or unit tests.

Requirements
- Python 3.7+ (uses modern type hints but no special libraries).

License
- Use/modify freely for learning and small projects.