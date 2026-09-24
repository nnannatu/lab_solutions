# ============================================================
# Task 2 — Passing a function as an argument
# ============================================================
# Create:
#
#   double(number)
#   triple(number)
#
# Then create:
#
#   apply(operation, value)
#
# apply() should call operation(value) and return the result.
#
# Examples:
# apply(double, 5) -> 10
# apply(triple, 5) -> 15
#
# Pass the function names WITHOUT parentheses.

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply(operation, value):
    return operation(value)


print(apply(double, 5))
print(apply(triple, 5))

