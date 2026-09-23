# ============================================================
# Task 2 — Default arguments
# ============================================================
# Create a function:
#
#   shipping_cost(weight, rate=2.5)
#
# It should return:
#   weight * rate
#
# Call it:
# 1. with only weight;
# 2. with a custom rate;
# 3. with rate passed as a keyword argument.
#
# Example:
# shipping_cost(4)
# returns 10.0

def shipping_cost(weight, rate=2.5):
    return weight * rate

print()

# with only weight
print(shipping_cost(5))
# with a custom rate
print(shipping_cost(7, 4.8))
# with rate passed as a keyword argument
print(shipping_cost(6, rate=7.5))
