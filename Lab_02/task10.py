print("Task 10 — Mutable and Immutable Objects")

# ----- LIST: mutable -----

numbers = [10, 20, 30]
# same_numbers points to the SAME list object, not a copy.
same_numbers = numbers

# Assigning to numbers[0] changes the underlying object.
numbers[0] = 99

print(f"numbers:      {numbers}")        # [99, 20, 30]
print(f"same_numbers: {same_numbers}")   # [99, 20, 30]
# Both changed because they refer to the same object.

# ----- STRING: immutable -----

text = "Python"
# same_text points to the same string object as text.
same_text = text

# Concatenation creates a NEW string and rebinds `text` to it.
# The original "Python" object is unchanged, so same_text is unaffected.
text = text + " Course"

print(f"text:      {text}")        # "Python Course"
print(f"same_text: {same_text}")   # "Python"
# Only `text` changed — strings are immutable.

print()