# ============================================================
# EXTRA Task 29 — Local maximum
# ============================================================
values = [3, 7, 4, 8, 5, 9, 2, 6, 1]

# A value is a local maximum if it is greater than both
# the value before it and the value after it.
#
# Do not check the first or last element.

# Start at index 1 and stop before the last index so both
# values[i - 1] and values[i + 1] are valid.
for i in range(1, len(values) - 1):
    if values[i] > values[i - 1] and values[i] > values[i + 1]:
        print(values[i])