from __future__ import annotations
import re
import string
import sys

def luhn_valid(card_number: str) -> bool:
    """Return True if card_number passes Luhn check. Non-digits are ignored."""
    digits = [int(ch) for ch in re.sub(r"\D", "", card_number)]
    if len(digits) < 2:
        return False
    check = digits.pop()  # last digit (rightmost) is the check digit
    # process from right to left, doubling every second digit
    digits.reverse()
    for i in range(len(digits)):
        if i % 2 == 0:  # positions 0,2,4... (originally every second from right)
            d = digits[i] * 2
            if d > 9:
                d -= 9
            digits[i] = d
    total = sum(digits) + check
    return total % 10 == 0

def remove_punctuation(text: str) -> str:
    """Return text with ASCII punctuation removed (keeps whitespace and other chars)."""
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def sort_sentence(sentence: str) -> str:
    """Return sentence with words sorted case-insensitively. Preserves single spaces."""
    words = [w for w in sentence.split() if w]
    words.sort(key=lambda w: w.lower())
    return " ".join(words)

def prompt(msg: str) -> str:
    """Safe input wrapper; exits on EOF/KeyboardInterrupt."""
    try:
        return input(msg)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        sys.exit(0)

def menu() -> None:
    while True:
        print("\nLAB TASK 4 — options:")
        print(" 1) Luhn card validation")
        print(" 2) Remove punctuation from text")
        print(" 3) Sort words in a sentence (alphabetical)")
        print(" 4) Quit")
        choice = prompt("Choose an option (1-4): ").strip()
        if choice == "1":
            card = prompt("Enter card number (digits, spaces or dashes allowed): ").strip()
            valid = luhn_valid(card)
            print("Valid" if valid else "Invalid")
        elif choice == "2":
            s = prompt("Enter text: ")
            print(remove_punctuation(s))
        elif choice == "3":
            s = prompt("Enter a sentence: ")
            print(sort_sentence(s))
        elif choice == "4" or choice.lower() in ("q", "quit", "exit"):
            print("Goodbye.")
            return
        else:
            print("Invalid option. Enter 1-4.")

if __name__ == "__main__":
    menu()