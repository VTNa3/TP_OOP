class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Dara", 80)

# Assignment operators
student1.score += 10
print("Updated score:", student1.score)

# Membership operators
students = ["Dara", "Sokha", "Vanna"]
print("Dara" in students)
print("Malis" not in students)

# Identity operator
student2 = student1
print(student1 is student2)

# Conditional expression
result = "Pass" if student1.score >= 50 else "Fail"
print("Result:", result)

# Operator precedence
total = 10 + 5 * 2
print("Total:", total)