# ============================================================
# Task 8 — Equality, identity, and references
# ============================================================
a = [10, 20]
b = [10, 20]
c = a

# Before running the program, predict:
#
# a == b
# a is b
# a == c
# a is c
#
# Print all four results.
#
# Then print:
#   id(a)
#   id(b)
#   id(c)
#
# Finally:
#   append 30 to c
#   print a
#   print b
#   print c
#
# Explain to yourself why a changes but b does not.

# a and b are separate lists with the same values
a = [10, 20]
b = [10, 20]
c = a  # c refers to the same object as a

# Equality vs identity checks
print(a == b)  # True  — same values
print(a is b)  # False — different objects
print(a == c)  # True  — same values
print(a is c)  # True  — same object

# Memory ids
print(id(a))
print(id(b))
print(id(c))

# Modify c (which is the same object as a)
c.append(30)

print(a)  # changed because c and a are the same object
print(b)  # unchanged because b is a different object
print(c)  # changed

# Explanation:
# c refers to the same object as a, so modifying c also
# modifies a. b is a separate object with the same values,
# so it does not change.