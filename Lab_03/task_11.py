# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores: print each one and accumulate the total.
#
# At the end print the count of valid scores and their average.
#
# Required:
# Use continue.

raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

total = 0
count = 0

for score in raw_scores:
    # Skip anything outside the valid range.
    if score < 0 or score > 100:
        continue

    # Only valid scores reach this point.
    print(score)
    total += score
    count += 1

# Average over valid scores only.
average = total / count

print("Valid scores:", count)
print(f"Average: {average:.2f}")