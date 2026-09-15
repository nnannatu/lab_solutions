# ============================================================
# EXTRA Task 32 — Find duplicate values
# ============================================================
numbers = [4, 7, 2, 4, 9, 7, 5, 2]

# Print every value that appears more than once.
#
# Do not print the same duplicate more than once.
#
# Do NOT use set() or .count().

for i in range(len(numbers)):
    # Check whether this value already appeared earlier —
    # if so, we've already handled it as a duplicate.
    already_reported = False
    for k in range(i):
        if numbers[k] == numbers[i]:
            already_reported = True
            break

    if already_reported:
        continue

    # Count occurrences of numbers[i] from i onward.
    count = 0
    for j in range(i, len(numbers)):
        if numbers[j] == numbers[i]:
            count += 1

    if count > 1:
        print(numbers[i])