class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

students = [Student("Ana", [90, 80]),
            Student("Ben", [70, 60])]

for s in students:
    avg = sum(s.grades) / len(s.grades)
    print(avg)  # 85.0, 65.0
for s in students:
    if s.name == "Ben":
        print("Found:", s.name)
        break
else:
    print("Not found")
