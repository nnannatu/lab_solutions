# ============================================================
# EXTRA Task 27 — Number frequency
# ============================================================
numbers = [4, 2, 7, 4, 8, 4, 2, 9, 4, 1]

# Ask the user for a number.
# Count how many times that number occurs.
#
# Do NOT use .count().

target = int(input("Enter a number: "))

occurrences = 0

for n in numbers:
    if n == target:
        occurrences += 1

print("Occurrences:", occurrences)