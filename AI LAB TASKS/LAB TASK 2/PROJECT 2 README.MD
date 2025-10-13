# Quratulain 
## roll no: 156 
### section : bsai 3c
****************************
# Mini Project 2 — Movie Budgets Analyzer

Overview
- Command-line Python script that analyzes a list of movies and their budgets.
- Lets the user add movies interactively and prints a budget report.

Files
- `mini project 2 .py` — main script containing:
  - Movie dataclass (title, budget)
  - DEFAULT_MOVIES list
  - Interactive prompts to add movies
  - Statistics and formatted report output

How it works
1. The script defines a Movie dataclass and a DEFAULT_MOVIES list.
2. `add_movies()` prompts the user to optionally add more movies (title + integer budget).
3. `compute_stats()` computes average budget and lists movies above/below average.
4. `print_report()` prints:
   - Total movies
   - Average budget (formatted)
   - Movies above/below average with differences
   - Highest and lowest budget movies
5. `main()` copies defaults, lets the user add movies, then prints the report.

Usage
- Run in a terminal:
  python "mini project 2 .py"
- While entering values, type `q`, `quit`, or `exit` to abort.

Notes
- Budgets are integers (USD).
- Output is printed to the console and formatted with thousands separators.
'@ | Out-File -FilePath "c:\Users\HAROON-CHISHTI\Desktop\AI LAB TASKS #3C\lab task 2\README.md" -Encoding utf8