# ============================================================
# Task 22 — Function: largest_of_three
# ============================================================
# Write a function:
#
#   largest_of_three(a, b, c)
#
# It should return the largest of the three numbers.
#
# Do NOT use:
#   max()
#
# Test with:
#
# largest_of_three(4, 9, 2)
# largest_of_three(10, 3, 10)
# largest_of_three(-1, -5, -3)
#
# Print the returned results.
# ============================================================

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(largest_of_three(4, 9, 2))
print(largest_of_three(10, 3, 10))
print(largest_of_three(-1, -5, -3))