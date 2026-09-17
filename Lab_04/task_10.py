# ============================================================
# Task 10 — Function: calculate_discount
# ============================================================
# Write a function:
#
#   calculate_discount(price, percent)
#
# It should return the final price after the discount.
#
# Formula:
# final_price = price - price * percent / 100
#
# Test it with:
#   calculate_discount(1000, 15)
#   calculate_discount(250, 20)
#
# Print each returned result.

# Return the price after applying a percentage discount
def calculate_discount(price, percent):
    return price - price * percent / 100


# Test the function
print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))