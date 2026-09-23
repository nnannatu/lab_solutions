# ============================================================
# Task 4 — *args: total score
# ============================================================
# Create a function:
#
#   total_score(*scores)
#
# Return the sum of all scores.
#
# The function must work with any number of arguments,
# including zero arguments.
#
# Examples:
# total_score(10, 20, 30) -> 60
# total_score(5)          -> 5
# total_score()           -> 0
#
# Inside the function, scores is a tuple.

def total_score(*scores):
    total = 0
    for score in scores:
        total = total + score
    
    return total

print(total_score(10, 20, 30))
print(total_score(5,))
print(total_score())
