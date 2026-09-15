# ============================================================
# EXTRA Task 34 — Detect first repeated value
# ============================================================
numbers = [5, 3, 8, 2, 3, 9, 5]

# Find the first value that appears for the second time.
# Stop searching immediately after finding it.

first_repeated = None

for i in range(len(numbers)):
    # Look for an earlier occurrence of the same value.
    for j in range(i):
        if numbers[j] == numbers[i]:
            first_repeated = numbers[i]
            break

    if first_repeated is not None:
        # Stop the outer loop as soon as a repeat is found.
        break

print("First repeated:", first_repeated)