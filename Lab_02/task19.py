# ============================================================
# Task 19 — Coordinate Analysis
# ============================================================

print("Task 19 — Coordinate Analysis")

# --- Read the four coordinates as floats ---
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# --- Group each point into a tuple ---
# Parentheses group the two numbers into an ordered, immutable pair.
point_1 = (x1, y1)
point_2 = (x2, y2)

# --- Calculate the differences ---
delta_x = x2 - x1
delta_y = y2 - y1

# --- Squared distance: Δx² + Δy² ---
distance_squared = delta_x ** 2 + delta_y ** 2

# --- Distance: square root = raise to the power of 0.5 ---
distance = distance_squared ** 0.5

# --- Print everything, distance to two decimals ---
print(f"Point 1: {point_1}")
print(f"Point 2: {point_2}")
print(f"Delta x: {delta_x}")
print(f"Delta y: {delta_y}")
print(f"Distance: {distance:.2f}")

print()