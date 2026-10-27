students = [
    {"name": "Dara", "scores": [90, 85, 95]},
    {"name": "Sokha", "scores": [60, 55, 65]}
]

for student in students:
    average = sum(student["scores"]) / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Name:", student["name"])
    print("Average:", average)
    print("Grade:", grade)

    if average >= 50:
        print("Status: Passed")
    else:
        print("Status: Failed")

    if average >= 85:
        print("Scholarship: Eligible")
    else:
        print("Scholarship: Not eligible")

    print("----------------")
