# ============================================================
# Task 5 — *args: average score
# ============================================================
# Create a function:
#
#   average_score(*scores)
#
# If no scores are given, return None.
# Otherwise return the arithmetic mean.
#
# Examples:
# average_score(80, 90, 100) -> 90.0
# average_score()             -> None

def average_score(*scores):
    if not scores:
        return None
    else:
        return sum(scores)/len(scores)
        

print(average_score(80, 90, 100))
print(average_score())