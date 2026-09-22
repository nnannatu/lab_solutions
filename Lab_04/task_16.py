# ============================================================
# Task 16 — Sum of even numbers with while
# ============================================================
# Ask the user for a positive integer n.
#
# Use a while loop to calculate the sum of all even numbers
# from 1 through n.
#
# Example:
# Input: 10
# Even sum: 30
#
# Because:
# 2 + 4 + 6 + 8 + 10 = 30
#
# Required:
# Use a while loop.
# ============================================================

n = int(input("Enter a positive integer: "))

total = 0
current = 2

while current <= n:
    total = total + current
    current = current + 2

print("Even sum:", total)