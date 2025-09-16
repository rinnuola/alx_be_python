# assign letter grade based on student score
score = 85  # directly using the score instead of asking for input

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
