# ============================================================
# Task 18 — Order Invoice
# ============================================================

print("Task 18 — Order Invoice")

# --- Read price and quantity for each of the three products ---
# Prices are floats (money can have decimals).
# Quantities are ints (you can't buy 2.5 items).

price_1 = float(input("Product 1 price: "))
quantity_1 = int(input("Product 1 quantity: "))

price_2 = float(input("Product 2 price: "))
quantity_2 = int(input("Product 2 quantity: "))

price_3 = float(input("Product 3 price: "))
quantity_3 = int(input("Product 3 quantity: "))

# --- Per-product subtotals: price * quantity ---
product_1_total = price_1 * quantity_1
product_2_total = price_2 * quantity_2
product_3_total = price_3 * quantity_3

# --- Order totals ---
subtotal = product_1_total + product_2_total + product_3_total

# Tax = 5% of the subtotal.
tax = subtotal * 0.05

# Final amount = subtotal + tax.
final_total = subtotal + tax

# --- Formatted invoice ---
# :.2f prints exactly two decimal places.
print(f"Product 1: {product_1_total:.2f}")
print(f"Product 2: {product_2_total:.2f}")
print(f"Product 3: {product_3_total:.2f}")
print("-" * 20)
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {final_total:.2f}")

print()