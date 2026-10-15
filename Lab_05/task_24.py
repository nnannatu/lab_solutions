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
    # Base case: no scores provided
    if not scores:
        return "No scores"

    # Seed trackers with the first score (avoids the "stuck at 0" trap)
    total = 0
    passed = 0
    failed = 0
    highest = scores[0]
    lowest = scores[0]

    # Single loop computes everything
    for score in scores:
        total = total + score

        if score >= passing:
            passed = passed + 1
        else:
            failed = failed + 1

        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    average = total / len(scores)

    return (
        f"{student}: average={average}, highest={highest}, "
        f"lowest={lowest}, passed={passed}, failed={failed}"
    )


# Test
print(exam_statistics("Anna", 80, 70, 50, 90, passing=60))
print(exam_statistics("Ben"))
print(exam_statistics("Cara", 100, 100, 100))
print(exam_statistics("Dan", 10, 20, 30))