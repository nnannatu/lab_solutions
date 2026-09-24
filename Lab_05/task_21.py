# ============================================================
# Task 21 — CHALLENGE: Recursive power
# ============================================================
# Create a recursive function:
#
#   power(base, exponent)
#
# Assume exponent is a non-negative integer.
#
# Rules:
# - if exponent == 0, return 1;
# - otherwise:
#
#     base^exponent =
#     base * base^(exponent - 1)
#
# Examples:
# power(2, 5)  -> 32
# power(3, 3)  -> 27
# power(10, 0) -> 1
#
# Do NOT use **.
# Do NOT use math.pow().
# Do NOT use a loop.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))
print(power(3, 3))
print(power(10, 0))