# Q6 Grade Calculator - Simple Version

print("GRADE CALCULATOR")
print("================")

# Get marks
s1 = float(input("Subject 1 marks: "))
s2 = float(input("Subject 2 marks: "))
s3 = float(input("Subject 3 marks: "))
s4 = float(input("Subject 4 marks: "))
s5 = float(input("Subject 5 marks: "))

# Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percent = (total / 500) * 100

# Check pass/fail
if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40:
    pass_fail = "PASS"
else:
    pass_fail = "FAIL"

# Find grade
if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B"
elif percent >= 60:
    grade = "C"
elif percent >= 50:
    grade = "D"
else:
    grade = "F"

# Show results
print("\n===== RESULTS =====")
print("Subject 1:", s1)
print("Subject 2:", s2)
print("Subject 3:", s3)
print("Subject 4:", s4)
print("Subject 5:", s5)
print("Total:", total, "/ 500")
print("Percentage:", round(percent, 2), "%")
print("Result:", pass_fail)
print("Grade:", grade)
print("==================")