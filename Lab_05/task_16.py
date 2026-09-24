# ============================================================
# Task 16 — Minimum and maximum with *args
# ============================================================
# Create a function:
#
#   score_range(*scores)
#
# If no scores are given, return None.
#
# Otherwise return the difference between
# the largest and smallest score.
#
# Do NOT use max() or min().
#
# Use a loop to find the smallest and largest values.
#
# Examples:
# score_range(10, 30, 20, 50) -> 40
# score_range(5)               -> 0
# score_range()                -> None
# ============================================================

def score_range(*scores):
    if not scores:
        return None

    smallest = scores[0]
    largest = scores[0]

    for score in scores:
        if score > largest:
            largest = score
        if score < smallest:
            smallest = score

    return largest - smallest


# Tests
print(score_range(10, 30, 20, 50))   # 40
print(score_range(5))                # 0
print(score_range())                 # None
print(score_range(-5, -1, -10))      # 9