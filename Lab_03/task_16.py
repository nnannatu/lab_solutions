# ============================================================
# EXTRA Task 16 — Number statistics
# ============================================================
numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

# Using one for loop, calculate:
#   number of positive values
#   number of negative values
#   number of zeros
#   sum of positive values
#   sum of negative values
#
# Expected:
# Positive: 5
# Negative: 3
# Zero: 2
# Positive sum: 63
# Negative sum: -15

positive_count = 0
negative_count = 0
zero_count = 0
positive_sum = 0
negative_sum = 0

for n in numbers:
    if n > 0:
        positive_count += 1
        positive_sum += n
    elif n < 0:
        negative_count += 1
        negative_sum += n
    else:
        zero_count += 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)
print("Positive sum:", positive_sum)
print("Negative sum:", negative_sum)