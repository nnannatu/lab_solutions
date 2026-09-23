# ============================================================
# Task 14 — BONUS: Student result summary
# ============================================================
# Create a function:
#
#   result_summary(name, *scores, passing=60)
#
# Requirements:
# - if no scores are given, return:
#     "No scores"
# - calculate the average;
# - count how many scores are >= passing;
# - return a string in this form:
#
#   "Anna: average=80.0, passed=3/4"
#
# Example:
# result_summary("Anna", 80, 70, 50, 120, passing=60)
#
# returns:
# "Anna: average=80.0, passed=3/4"
#
# Use a loop to count passed scores.
# Do not use filter() or map().

def result_summary(name, *scores, passing=60):
    count = 0
    average = 0
    if not scores:
        return "No scores"
    elif 
    