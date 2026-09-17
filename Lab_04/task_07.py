# ============================================================
# Task 7 — Dynamic typing
# ============================================================
# Create a variable named value.
#
# First assign:
#   42
# Print the value and its type.
#
# Then assign:
#   3.14
# Print the value and its type.
#
# Then assign:
#   "Python"
# Print the value and its type.
#
# Finally assign:
#   [1, 2, 3]
# Print the value and its type.
#
# Observe that the same variable name can refer to objects
# of different types during program execution.

# Assign an integer
value = 42
print(value, type(value))

# Reassign to a float
value = 3.14
print(value, type(value))

# Reassign to a string
value = "Python"
print(value, type(value))

# Reassign to a list
value = [1, 2, 3]
print(value, type(value))