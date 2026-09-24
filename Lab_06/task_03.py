# ============================================================
# Task 3 — Higher-order function
# ============================================================
# Create:
#
#   transform(values, operation)
#
# It should:
# - create an empty result list;
# - loop through values;
# - apply operation() to each value;
# - append each result;
# - return the new list.
#
# Then create:
#
#   square(number)
#
# Test:
# transform([1, 2, 3, 4], square)
#
# Expected:
# [1, 4, 9, 16]
# ============================================================

def transform(values, operation):
    result_list = []
    for value in values:
        result_list.append(operation(value))
    return result_list


def square(number):
    return number ** 2


# Test
print(transform([1, 2, 3, 4], square))