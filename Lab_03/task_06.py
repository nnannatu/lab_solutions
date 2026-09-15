# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683


total = 0                                

for number in range(3, 100, 3):               
    total += number                           

print(total)    