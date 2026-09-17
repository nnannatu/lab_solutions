# ============================================================
# BONUS Task 15 — Function-based number statistics
# ============================================================
# Write a function:
#
#   number_statistics(numbers)
#
# It should use a loop to count:
#   positive numbers
#   negative numbers
#   zeros
#
# Return all three counts.
#
# Test with:
# data = [3, -1, 0, 8, -5, 0, 2, -9]
#
# Print:
#   Positive: ...
#   Negative: ...
#   Zero: ...
#
# Do not use list comprehensions.

# Count positives, negatives, and zeros in a list
def number_statistics(numbers):
    positive = 0
    negative = 0
    zero = 0

    for num in numbers:
        if num > 0:
            positive = positive + 1
        elif num < 0:
            negative = negative + 1
        else:
            zero = zero + 1

    return positive, negative, zero


# Test data
data = [3, -1, 0, 8, -5, 0, 2, -9]
positive, negative, zero = number_statistics(data)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)