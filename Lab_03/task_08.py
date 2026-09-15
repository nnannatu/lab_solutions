# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

text = input("Enter a word or short text: ").lower()

vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(count)