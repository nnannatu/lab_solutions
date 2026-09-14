# ============================================================
# Task 22 — Debug the Program
# ============================================================

print("Task 22 — Debug the Program")

# --- Fixed version ---
#
# Original problems:
#   1. input() returns a string — needs float() for arithmetic.
#   2. Inconsistent casing: score1, Score2, score3 — should all
#      be lowercase (PEP 8 uses snake_case for variables).
#   3. `total=score1+Score2+score3` concatenates strings, not adds numbers.
#   4. `print("Average:"+average)` tries to concatenate str + float — TypeError.
#   5. No spaces around `=` or `+` — PEP 8 violation.
#   6. No formatted output for the average.

score_1 = float(input("Score 1: "))
score_2 = float(input("Score 2: "))
score_3 = float(input("Score 3: "))

total = score_1 + score_2 + score_3
average = total / 3

print(f"Average: {average:.2f}")

print()