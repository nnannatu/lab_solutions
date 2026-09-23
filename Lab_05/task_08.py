# ============================================================
# Task 8 — Scope
# ============================================================
# Create a global variable:
#
#   TAX_RATE = 0.20
#
# Create a function:
#
#   final_price(price)
#
# Inside the function:
# 1. calculate a LOCAL variable called tax;
# 2. return price + tax.
#
# Do not modify TAX_RATE.
#
# Example:
# final_price(100) -> 120.0
#
# Think about:
# - TAX_RATE is global.
# - tax exists only inside final_price().

TAX_RATE = 0.20

def final_price(price):
    tax = price * TAX_RATE
    return price + tax

print(final_price(100))