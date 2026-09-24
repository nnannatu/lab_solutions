# ============================================================
# Task 6 — Descending order
# ============================================================
# Start with:
#
# scores = [82, 95, 73, 88, 61]
#
# Use sorted() with reverse=True.
#
# Store the result in:
#
#   high_to_low
#
# Expected:
# [95, 88, 82, 73, 61]
#
# The original scores list should remain unchanged.

scores = [82, 95, 73, 88, 61]

high_to_low = sorted(scores, reverse=True)

print("scores:      ", scores)
print("high_to_low: ", high_to_low)


