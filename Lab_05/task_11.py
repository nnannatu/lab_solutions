# ============================================================
# Task 11 — Recursive sum
# ============================================================
# Create a recursive function:
#
#   sum_to(n)
#
# It should return:
#   1 + 2 + 3 + ... + n
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 0;
# - otherwise use recursion.
#
# Do NOT use a loop and do NOT use sum().
#
# Examples:
# sum_to(4) -> 10
# sum_to(0) -> 0

def sum_to(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    else:
        return n + sum_to(n-1)

print(sum_to(4))
print(sum_to(0))