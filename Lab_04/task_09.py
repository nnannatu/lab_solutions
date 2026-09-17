# ============================================================
# Task 9 — Function: is_even
# ============================================================
# Write a function:
#
#   is_even(number)
#
# It should return:
#   True  if number is even
#   False otherwise
#
# Then call it with:
#   4
#   7
#   0
#
# Print the returned results.
#
# IMPORTANT:
# The function must return the Boolean result.
# Do not print from inside the function.

# Return True if number is even, False otherwise
def is_even(number):
    return number % 2 == 0


# Test the function
print(is_even(4))
print(is_even(7))
print(is_even(0))