# ============================================================
# Task 19 — math: distance between two points
# ============================================================
# Create a function:
#
#   distance(x1, y1, x2, y2)
#
# Calculate the Euclidean distance between two points.
#
# Formula:
#
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#
# Use math.sqrt().
#
# Example:
# distance(0, 0, 3, 4) -> 5.0

import math

def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return distance

print(distance(0, 0, 3, 4))