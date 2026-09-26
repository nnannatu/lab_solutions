# ============================================================
# Task 8 — Case-insensitive sorting
# ============================================================
# Start with:
#
# cities = [
#     "berlin",
#     "Algiers",
#     "cairo",
#     "Amsterdam",
#     "zurich"
# ]
#
# Sort the list alphabetically without treating uppercase
# and lowercase letters as separate groups.
#
# Use:
#
#   key=str.lower
#
# Store the result in:
#
#   ordered_cities
#
# The original capitalization must stay unchanged.

cities = [
     "berlin",
     "Algiers",
     "cairo",
     "Amsterdam",
     "zurich"
 ]

ordered_cities = sorted(cities, key=str.lower)

print(ordered_cities)
