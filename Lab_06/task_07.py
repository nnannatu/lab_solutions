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

words = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first = words[0]
longest_first = words[0]

for word in words:
    if len(word) < shortest_first:
        
