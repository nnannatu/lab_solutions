# ============================================================
# EXTRA Task 36 — Number triangle
# ============================================================
# Print:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Required:
# Use nested for loops.

for row in range(1, 6):
    line_parts = []
    for column in range(1, row + 1):
        line_parts.append(str(column))

    print(" ".join(line_parts))