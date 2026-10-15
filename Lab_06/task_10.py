# ============================================================
# Task 10 — Filtering values
# ============================================================
# Start with:
#
# scores = [45, 70, 82, 39, 91, 60, 58]
#
# Use filter() and a lambda to keep only scores >= 60.
#
# Convert the filter result to a list.
#
# Expected:
# [70, 82, 91, 60]

scores = [45, 70, 82, 39, 91, 60, 58]

filtered_result = []
filtered_resul = filter(scores, lambda s: s >= 60)
