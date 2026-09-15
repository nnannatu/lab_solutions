# ============================================================
# EXTRA Task 24 — Multiplication table
# ============================================================
# Print a multiplication table from 1 to 5.
#
# Required:
# Use nested for loops.

for row in range(1, 6):
    # Build the row as a list of strings, then join with
    # a space so every value stays aligned in one line.
    line_parts = []
    for column in range(1, 6):
        line_parts.append(str(row * column))

    print(" ".join(line_parts))