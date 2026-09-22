# ============================================================
# Task 19 — Count positive values
# ============================================================
numbers = [5, -2, 0, 8, -4, 11, 0, -1, 7]

# Use a loop to count how many values are:
#
#   positive
#   negative
#   zero
#
# Print:
#
# Positive: ...
# Negative: ...
# Zero: ...
#
# Do not use list comprehensions.
# ============================================================

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)