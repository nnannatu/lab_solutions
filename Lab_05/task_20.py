# ============================================================
# Task 20 — List operations: shopping list
# ============================================================
# Start with:
#
# shopping = ["bread", "milk", "eggs"]
#
# Perform these operations in order:
#
# 1. append "rice"
# 2. insert "coffee" at index 1
# 3. extend the list with ["tea", "sugar"]
# 4. remove "milk"
# 5. print the index of "eggs"
# 6. print how many times "bread" appears
# 7. pop the last item and store it in removed_item
# 8. print the final shopping list
# 9. print removed_item
#
# Expected final list:
# ["bread", "coffee", "eggs", "rice", "tea"]

shopping = ["bread", "milk", "eggs"]

shopping.append("rice")

shopping.insert(1, "coffee")

shopping.extend(["tea", "sugar"])

shopping.remove("milk")

print("Index of Eggs:", shopping.index("eggs"))
print("Count of Bread:", shopping.count("bread"))

removed_item = shopping.pop()
print(shopping)
print(removed_item)