print("Task 2 — Absolute Value and Rounding")

# A negative float — represents a temperature drop.
temperature_change = -7.438

# A float with many decimal places — needs rounding.
measurement = 19.87654

# abs() returns the magnitude (non-negative value).
# abs(-7.438) -> 7.438
print(f"Absolute value: {abs(temperature_change)}")

# round(x, n) rounds to n decimal places.
# round(x) with no second argument rounds to the nearest integer.
print(f"Rounded to 1 decimal:  {round(measurement, 1)}")   # 19.9
print(f"Rounded to 2 decimals: {round(measurement, 2)}")   # 19.88
print(f"Rounded to 3 decimals: {round(measurement, 3)}")   # 19.877

print()
