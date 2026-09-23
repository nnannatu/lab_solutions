# ============================================================
# Task 13 — BONUS: Recursive digit sum
# ============================================================
# Create a recursive function:
#
#   digit_sum(n)
#
# Assume n is a non-negative integer.
#
# Return the sum of its digits.
#
# Hint:
# - last digit: n % 10
# - remaining digits: n // 10
#
# Base case:
# if n < 10, return n
#
# Examples:
# digit_sum(1234) -> 10
# digit_sum(7)    -> 7
#
# Do NOT convert the number to a string.
# Do NOT use a loop.


def digit_sum(n):
    if n < 10:
        return n
    
    return (n % 10) + digit_sum(n // 10)

print(digit_sum(1234))
print(digit_sum(7))
print(digit_sum(0))