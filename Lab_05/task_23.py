# ============================================================
# Task 23 — CHALLENGE: Recursive list sum
# ============================================================
# Create a recursive function:
#
#   recursive_sum(numbers)
#
# Return the sum of all numbers in the list.
#
# Examples:
# recursive_sum([10, 20, 30]) -> 60
# recursive_sum([5])          -> 5
# recursive_sum([])           -> 0
#
# Hint:
#
# Base case:
# if the list is empty:
#     return 0
#
# Recursive idea:
#
# first element + sum of the remaining elements
#
# Do NOT use:
# - sum()
# - for
# - while

def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum([10, 20, 30]))
print(recursive_sum([5]))
print(recursive_sum([]))