# ============================================================
# Task 10 — Recursive factorial
# ============================================================
# Create a recursive function:
#
#   factorial(n)
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 1;
# - otherwise return n * factorial(n - 1).
#
# Do NOT use a loop.
#
# Examples:
# factorial(5)  -> 120
# factorial(0)  -> 1
# factorial(-2) -> None


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(0))
print(factorial(-2))