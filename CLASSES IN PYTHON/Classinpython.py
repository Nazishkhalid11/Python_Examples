class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks < 50:
            return "FAIL"
        else:
            return "PASS"

students = [
    Student("Guriya", 50),
    Student("John", 40),
    Student("Jane", 60)
]

teacher_likes = []

for student in students:
    print(student.name, "is", student.result())
    if student.result() == "PASS":
        teacher_likes.append(student.name)

print("Teacher likes:", teacher_likes)
