from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
import sys

@dataclass
class Movie:
    title: str
    budget: int

DEFAULT_MOVIES: List[Movie] = [
    Movie("Eternal Sunshine of the Spotless Mind", 20_000_000),
    Movie("Memento", 9_000_000),
    Movie("Requiem for a Dream", 45_000_000),
    Movie("Pirates of the Caribbean: On Stranger Tides", 379_000_000),
    Movie("Avengers: Age of Ultron", 365_000_000),
    Movie("Avengers: Endgame", 356_000_000),
    Movie("Incredibles 2", 200_000_000),
]

def prompt_int(prompt: str, min_value: int = 0) -> int:
    while True:
        try:
            raw = input(prompt).strip()
            if raw.lower() in ("q", "quit", "exit"):
                print("Exiting.")
                sys.exit(0)
            v = int(raw)
            if v < min_value:
                print(f"Enter an integer >= {min_value}.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def prompt_str(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter a non-empty value.")
            continue
        if s.lower() in ("q", "quit", "exit"):
            print("Exiting.")
            sys.exit(0)
        return s

def add_movies(base: List[Movie]) -> List[Movie]:
    n = prompt_int("How many movies do you want to add? (0 for none): ", 0)
    for i in range(n):
        title = prompt_str(f"Movie #{i+1} title: ")
        budget = prompt_int(f"Movie #{i+1} budget (USD, integer): ", 0)
        base.append(Movie(title, budget))
    return base

def compute_stats(movies: List[Movie]) -> Tuple[float, List[Tuple[Movie,float]], List[Tuple[Movie,float]]]:
    if not movies:
        return 0.0, [], []
    avg = sum(m.budget for m in movies) / len(movies)
    above = [(m, m.budget - avg) for m in movies if m.budget > avg]
    below = [(m, avg - m.budget) for m in movies if m.budget < avg]
    return avg, sorted(above, key=lambda x: -x[0].budget), sorted(below, key=lambda x: -x[0].budget)

def format_money(n: float) -> str:
    return f"${n:,.0f}"

def print_report(movies: List[Movie]) -> None:
    avg, above, below = compute_stats(movies)
    print("\n--- Movies Summary ---")
    print(f"Total movies : {len(movies)}")
    print(f"Average budget: {format_money(avg)}")
    if above:
        print(f"\nMovies above average ({len(above)}):")
        for m, diff in above:
            print(f"  {m.title} — {format_money(m.budget)} (above by {format_money(diff)})")
    else:
        print("\nNo movies above average.")
    if below:
        print(f"\nMovies below average ({len(below)}):")
        for m, diff in below:
            print(f"  {m.title} — {format_money(m.budget)} (below by {format_money(diff)})")
    # show top and bottom
    top = max(movies, key=lambda m: m.budget)
    bottom = min(movies, key=lambda m: m.budget)
    print(f"\nHighest budget : {top.title} — {format_money(top.budget)}")
    print(f"Lowest budget  : {bottom.title} — {format_money(bottom.budget)}")

def main() -> None:
    movies: List[Movie] = DEFAULT_MOVIES.copy()
    try:
        movies = add_movies(movies)
    except SystemExit:
        return
    print_report(movies)

if __name__ == "__main__":
    main()