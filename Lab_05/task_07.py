# ============================================================
# Task 7 — Combining fixed arguments, *args, and **kwargs
# ============================================================
# Create a function:
#
#   course_report(student, *scores, **options)
#
# It should print:
#   Student: ...
#   Scores: (...)
#   Options: {...}
#
# Example:
# course_report(
#     "Mira",
#     80, 92, 75,
#     rounded=True,
#     scale=100
# )
#
# Expected structure:
# Student: Mira
# Scores: (80, 92, 75)
# Options: {'rounded': True, 'scale': 100}

def course_report(student, *scores, **options):
    print("student:", student)
    print("Scores:", scores)
    print("Options:", options)


course_report(
    "Mira",
    80, 92, 75,
    rounded=True,
    scale=100
    )