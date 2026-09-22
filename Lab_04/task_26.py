# ============================================================
# Task 26 — Reverse counting pattern
# ============================================================
# Ask the user for a positive integer n.
#
# Print this pattern using nested loops.
#
# Example for n = 5:
#
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
#
# Required:
# Use nested loops.
#
# Hint:
# Think about:
#   outer loop -> controls the row
#   inner loop -> prints values inside the row
# ============================================================

n = int(input("Enter a positive integer: "))

for row in range(1, n + 1):
    for value in range(row, 0, -1):
        print(value, end=" ")
    print()