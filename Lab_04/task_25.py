# ============================================================
# Task 25 — Function: count_even
# ============================================================
# Write a function:
#
#   count_even(numbers)
#
# It receives a list of integers.
#
# Count how many values are even and return the count.
#
# Test with:
#
# values = [4, 7, 10, 13, 16, 19, 20]
#
# Expected result:
# 4
#
# The function must return the result.
# ============================================================

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count

values = [4, 7, 10, 13, 16, 19, 20]
print(count_even(values))