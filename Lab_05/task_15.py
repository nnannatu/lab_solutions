# ============================================================
# Task 15 — Function with validation
# ============================================================
# Create a function:
#
#   calculate_discount(price, discount=10)
#
# Requirements:
# - price must be greater than 0;
# - discount must be between 0 and 100.
#
# If the values are invalid, return None.
#
# Otherwise return the final price after applying the discount.
#
# Formula:
# final_price = price - price * discount / 100
#
# Examples:
# calculate_discount(100)      -> 90.0
# calculate_discount(200, 25)  -> 150.0
# calculate_discount(100, 120) -> None
# calculate_discount(-20, 10)  -> None


def calculate_discount(price, discount=10):
    # price must be greater than 0
    if price <= 0:
        return None

    # discount must be between 0 and 100
    if discount < 0 or discount > 100:
        return None

    final_price = price - price * discount / 100
    return final_price


# Tests
print(calculate_discount(100))       # 90.0
print(calculate_discount(200, 25))   # 150.0
print(calculate_discount(100, 120))  # None
print(calculate_discount(-20, 10))   # None
