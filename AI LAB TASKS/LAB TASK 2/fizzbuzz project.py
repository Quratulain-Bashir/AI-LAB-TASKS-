
from __future__ import annotations
import argparse
import random
import time
from typing import List, Tuple

def fizzbuzz_value(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def run_quiz(numbers: List[int]) -> Tuple[int,int,list]:
    score = 0
    attempts = 0
    wrong = []
    for i in numbers:
        correct = fizzbuzz_value(i)
        ans = input(f"{i}: ").strip()
        if not ans:
            print("Empty input — skipped.")
            continue
        if ans.lower() in ("q", "quit"):
            print("Quitting early.")
            break
        attempts += 1
        if ans.lower() == correct.lower():
            score += 1
            print("✓")
        else:
            wrong.append((i, ans, correct))
            print("✗")
    return score, attempts, wrong

def run_learn(numbers: List[int]) -> Tuple[int,int,list]:
    score = 0
    attempts = 0
    wrong = []
    for i in numbers:
        correct = fizzbuzz_value(i)
        ans = input(f"{i}: ").strip()
        if not ans:
            print(f"Empty — answer: {correct}")
            continue
        if ans.lower() in ("q", "quit"):
            print("Quitting early.")
            break
        attempts += 1
        if ans.lower() == correct.lower():
            score += 1
            print("Correct ✅")
        else:
            wrong.append((i, ans, correct))
            print(f"Wrong — correct: {correct}")
    return score, attempts, wrong

def show_sequence(numbers: List[int]) -> None:
    for i in numbers:
        print(f"{i}: {fizzbuzz_value(i)}")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Mini FizzBuzz — quiz/practice/show")
    p.add_argument("--max", "-n", type=int, default=100, help="Max number (default 100)")
    p.add_argument("--mode", "-m", choices=("quiz","learn","show"), default="quiz", help="Mode")
    p.add_argument("--shuffle", action="store_true", help="Shuffle the sequence")
    return p.parse_args()

def main() -> None:
    args = parse_args()
    nums = list(range(1, max(1, args.max) + 1))
    if args.shuffle:
        random.shuffle(nums)

    start = time.perf_counter()
    if args.mode == "show":
        show_sequence(nums)
        score = attempts = 0
        wrong = []
    elif args.mode == "learn":
        score, attempts, wrong = run_learn(nums)
    else:  # quiz
        score, attempts, wrong = run_quiz(nums)
    elapsed = time.perf_counter() - start

    print("\n--- Summary ---")
    print(f"Mode      : {args.mode}")
    print(f"Items     : {len(nums)}")
    print(f"Attempts  : {attempts}")
    print(f"Score     : {score}")
    print(f"Accuracy  : { (score/attempts*100):.1f}% " if attempts else "Accuracy  : N/A")
    print(f"Time      : {elapsed:.2f}s")
    if wrong:
        print("\nIncorrect answers:")
        for i, given, correct in wrong:
            print(f" {i}: you='{given}' expected='{correct}'")

if __name__ == "__main__":
    main()


