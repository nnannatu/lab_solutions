# ============================================================
# EXTRA Task 22 — Count increases
# ============================================================
values = [10, 14, 13, 18, 22, 20, 25, 25, 30]

# Count how many times a value is greater than the value
# immediately before it.
#
# Expected:
# Increases: 5

increases = 0

# Start at index 1 so values[i - 1] is always valid.
for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increases += 1

print("Increases:", increases)