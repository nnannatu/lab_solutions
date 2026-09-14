print("Task 6 — Type Conversion")

# Original float with a fractional part.
value = 17.95

# int() chops off the decimal part — it does NOT round.
# int(17.95) -> 17   (not 18)
integer_value = int(value)
print(f"int(value): {integer_value}")     # 17

# Converting the int back to float gives 17.0, not 17.95.
# The fractional part is gone forever — the round trip
# is not reversible.
float_value = float(integer_value)
print(f"float(integer_value): {float_value}")     # 17.0

# str() converts a number into text.
# type() tells us the data type of the object.
text_value = str(integer_value)
print(f"Value as text: {text_value}")             # "17"
print(f"Type: {type(text_value)}")                # <class 'str'>

print()