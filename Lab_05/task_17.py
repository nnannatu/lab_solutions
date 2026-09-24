# ============================================================
# Task 17 — Count values above a limit
# ============================================================
# Create a function:
#
#   count_above(limit, *numbers)
#
# Return how many numbers are greater than limit.
#
# Examples:
# count_above(10, 5, 12, 30, 7, 20) -> 3
# count_above(100, 10, 20, 30)       -> 0
# count_above(5)                      -> 0
#
# Use a loop.

def count_above(limit, *numbers):
    
    count = 0
    for number in numbers:
        if number > limit:
            count = count + 1
    
    return count


print(count_above(10, 5, 12, 30, 7, 20))
print(count_above(100, 10, 20, 30))
print(count_above(5))