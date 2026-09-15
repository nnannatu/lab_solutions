# ============================================================
# EXTRA Task 26 — Count consecutive positives
# ============================================================
numbers = [2, 5, 7, -1, 3, 4, 8, 9, -2, 6]

# Find the longest sequence of consecutive positive numbers.
#
# Expected:
# Longest positive sequence: 4

current_count = 0
longest_count = 0

for n in numbers:
    if n > 0:
        current_count += 1
        if current_count > longest_count:
            longest_count = current_count
    else:
        # A non-positive value breaks the current streak.
        current_count = 0

print("Longest positive sequence:", longest_count)