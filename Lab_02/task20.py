# ============================================================
# Task 20 — Complex Numbers
# ============================================================

print("Task 20 — Complex Numbers")

# Two complex numbers. j is Python's imaginary unit (i in math).
z1 = 3 + 4j
z2 = 2 - 1j

# The value and type of z1.
print(f"z1: {z1}")
print(f"z2: {z2}")
print(f"type(z1): {type(z1)}")

# --- Arithmetic on complex numbers ---
# All four operations return complex numbers.
print(f"z1 + z2: {z1 + z2}")     # (5+3j)
print(f"z1 - z2: {z1 - z2}")     # (1+5j)
print(f"z1 * z2: {z1 * z2}")     # (10+5j)
print(f"z1 / z2: {z1 / z2}")     # (0.4+2.2j)

# --- Real and imaginary parts ---
# .real and .imag are read-only attributes of a complex number.
print(f"z1.real: {z1.real}")     # 3.0
print(f"z1.imag: {z1.imag}")     # 4.0

print()