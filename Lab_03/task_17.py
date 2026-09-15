# ============================================================
# EXTRA Task 17 — Highest and lowest score
# ============================================================
scores = [71, 85, 42, 96, 58, 83, 67, 91]

# Find the highest and lowest scores using a for loop.
#
# Do NOT use max(), min() or sorted().

# Seed both trackers with the first element so every
# subsequent value can be compared against them.
highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

print("Highest:", highest)
print("Lowest:", lowest)