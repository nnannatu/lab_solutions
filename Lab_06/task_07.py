# ============================================================
# Task 7 — Sorting with key
# ============================================================
# Start with:
#
# words = ["pear", "watermelon", "fig", "banana", "kiwi"]
#
# Create:
#
#   shortest_first
#   longest_first
#
# shortest_first:
# sort by string length from shortest to longest.
#
# longest_first:
# sort by string length from longest to shortest.
#
# Use key=len for at least one of the two results.
#
# Do not manually calculate the lengths.
# ============================================================

words = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first = sorted(words, key=len)
longest_first = sorted(words, key=len, reverse=True)

print("Shortest first:", shortest_first)
print("Longest first: ", longest_first)