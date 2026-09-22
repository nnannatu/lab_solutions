# ============================================================
# Task 27 — Function: classify_number
# ============================================================
# Write a function:
#
#   classify_number(number)
#
# It should return one of these strings:
#
#   "Positive even"
#   "Positive odd"
#   "Negative even"
#   "Negative odd"
#   "Zero"
#
# Examples:
#
# classify_number(8)   -> "Positive even"
# classify_number(-3)  -> "Negative odd"
# classify_number(0)   -> "Zero"
#
# Test the function with several numbers.
# ============================================================

def classify_number(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        if number % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        if number % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"

print(classify_number(8))
print(classify_number(-3))
print(classify_number(0))
print(classify_number(7))
print(classify_number(-4))