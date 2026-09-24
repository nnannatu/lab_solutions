# ============================================================
# Task 24 — CHALLENGE: Exam statistics
# ============================================================
# Create a function:
#
#   exam_statistics(student, *scores, passing=60)
#
# If no scores are provided, return:
#
#   "No scores"
#
# Otherwise calculate:
#
# - average score
# - highest score
# - lowest score
# - number of passed scores
# - number of failed scores
#
# Do NOT use:
# - min()
# - max()
# - sum()
#
# Calculate everything using a loop.
#
# Return a string like:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"
#
# Example:
#
# exam_statistics(
#     "Anna",
#     80, 70, 50, 90,
#     passing=60
# )
#
# returns:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"

def exam_statistics(student, *scores, passing=60):
    if not scores:
        return "No scores"

    passed = 0,
    failed = 0,
    total = 0,
    average_score = 0,
    lowest_score = 0,
    highest_score = 0,

    for score in scores:
        total = total + score
        if score > 60:
            passed = passed + 1
        else:
            failed = failed + 1
        if score < lowest_score:
            lowest_score = score
        else:
            highest_score = score

    average_score = 