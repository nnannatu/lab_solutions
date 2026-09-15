# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:
score = int(input("Enter a score: "))    

if score < 0 or score > 100:             
    print("Invalid score")
elif score >= 90:                        
    print("A")
elif score >= 75:
        print("B")
elif score >= 60:                        
    print("C")
else:                                    
    print("Fail")