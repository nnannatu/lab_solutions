# ============================================================
# EXTRA Task 25 — Second largest value
# ============================================================
numbers = [12, 7, 19, 3, 19, 14, 8]

# Find the second largest DISTINCT value.
#
# Expected:
# Second largest: 14
#
# Do NOT use sorted() or max().

largest = None
second_largest = None

for n in numbers:
    if largest is None or n > largest:
        # A new largest pushes the old largest to second place.
        second_largest = largest
        largest = n
    elif n != largest and (second_largest is None or n > second_largest):
        # Only distinct values below the largest are considered.
        second_largest = n

print("Second largest:", second_largest)