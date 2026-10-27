students = {
    "01": {
        "name": "Dara",
        "age": 18,
        "score": 85
    },                         #list of students in set
    "02": {
        "name": "Sokha",
        "age": 19,
        "score": 90.2
    },
    "03": {
        "name": "Vanna",
        "age": 20,
        "score": 78
    }
}

for student_id, student in students.items():    # Display all records
    print("Student ID:", student_id)
    print("Name:", student["name"])     #str
    print("Age:", student["age"])       #int
    print("Score:", student["score"])   #float
    print("----------------")