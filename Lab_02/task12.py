print("Task 12 — PEP 8 Cleanup")

unit_price = 1250          # price per unit
quantity = 3               # number of units
discount_rate = 10         # discount percentage (10%)

# Subtotal before discount: P * Q
subtotal = unit_price * quantity

# Discount amount: D/100 * subtotal
discount_amount = discount_rate / 100 * subtotal

# Final price: subtotal - discount
final_price = subtotal - discount_amount

# Formatted output using an f-string.
print(f"Final: {final_price}")

print()