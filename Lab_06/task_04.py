# ============================================================
# Task 4 — Lambda expressions
# ============================================================
# Create these lambda functions:
#
#   double
#   add
#   is_even
#
# Requirements:
# double(5)    -> 10
# add(3, 4)    -> 7
# is_even(8)   -> True
# is_even(7)   -> False
#
# Each lambda must contain only one expression.


double = lambda number: number * 2

add = lambda a, b: a + b

is_even = lambda number: number % 2 == 0


# Tests
print(double(5))     # 10
print(add(3, 4))     # 7
print(is_even(8))    # True
print(is_even(7))    # False