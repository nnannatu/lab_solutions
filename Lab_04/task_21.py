# ============================================================
# Task 21 — Function: absolute_value
# ============================================================
# Write a function:
#
#   absolute_value(number)
#
# It should return the absolute value of the number.
#
# Examples:
#
# absolute_value(5)   -> 5
# absolute_value(-8)  -> 8
# absolute_value(0)   -> 0
#
# Do NOT use:
#   abs()
#
# Test the function with:
#   10
#   -7
#   0
#
# Print the returned values.
# ============================================================

def absolute_value(number):
    if number < 0:
        return -number
    return number

print(absolute_value(10))
print(absolute_value(-7))
print(absolute_value(0))