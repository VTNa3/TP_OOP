class Student:
    school_name = "Institute of Technology of Cambodia"  # Shared attribute

    def __init__(self, name, age, score):
        self.name = name      # Individual attribute
        self.age = age        # Individual attribute
        self.score = score    # Individual attribute

student1 = Student("Dara", 18, 85)  # Create student objects
student2 = Student("Sokha", 19, 90)
student3 = Student("Vanna", 20, 78)

print(student1.name, student1.age, student1.score, student1.school_name)    # Display student records
print(student2.name, student2.age, student2.score, student2.school_name)
print(student3.name, student3.age, student3.score, student3.school_name)