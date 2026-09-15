# ============================================================
# Task 7 — Count number categories
# ============================================================
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

positives = 0                            
negatives = 0                            
zeros = 0                               

for n in numbers:
    if n > 0:
        positives += 1
    elif n < 0:
        negatives += 1
    else:
        zeros += 1

print("Positive:", positives)
print("Negative:", negatives)
print("Zero:", zeros)