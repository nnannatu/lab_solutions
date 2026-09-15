# ============================================================
# EXTRA Task 18 — Temperature analysis
# ============================================================
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]

# Classify every temperature:
#
#   Cold -> below 10
#   Mild -> 10–19
#   Warm -> 20–29
#   Hot  -> 30 or above
#
# After processing, print how many temperatures fall
# into each category.

cold_count = 0
mild_count = 0
warm_count = 0
hot_count = 0

for temp in temperatures:
    if temp < 10:
        category = "Cold"
        cold_count += 1
    elif temp < 20:
        category = "Mild"
        mild_count += 1
    elif temp < 30:
        category = "Warm"
        warm_count += 1
    else:
        category = "Hot"
        hot_count += 1

    print(f"{temp}: {category}")

print("Cold:", cold_count)
print("Mild:", mild_count)
print("Warm:", warm_count)
print("Hot:", hot_count)