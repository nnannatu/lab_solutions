# ============================================================
# Task 22 — CHALLENGE: Recursive digit counter
# ============================================================
# Create a recursive function:
#
#   count_digits(n)
#
# Assume n is a non-negative integer.
#
# Return the number of digits in n.
#
# Examples:
# count_digits(7)     -> 1
# count_digits(1234)  -> 4
# count_digits(10000) -> 5
#
# Hint:
# Remove the last digit with:
#
#   n // 10
#
# Base case:
# if n < 10:
#     return 1
#
# Do NOT convert n to a string.
# Do NOT use a loop.

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(7))
print(count_digits(1234))
print(count_digits(10000))