# ============================================================
# Task 9 — Sorting tuples with lambda
# ============================================================
# Start with:
#
# students = [
#     ("Anna", 82),
#     ("Boris", 95),
#     ("Mira", 88),
#     ("Daniel", 73)
# ]
#
# Sort students by score from highest to lowest.
#
# Use:
#
#   sorted()
#   key=lambda ...
#   reverse=True

# Expected first item:
# ("Boris", 95)

students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]

organized = sorted(students, key=lambda s: s[1], reverse=True)

print(organized)