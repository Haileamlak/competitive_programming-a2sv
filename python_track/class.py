class Student:
    def __init__(self, s_name, s_major, s_gpa) -> None:
        self.name = s_name
        self.major = s_major
        self.gpa = s_gpa

student1 = Student("Abebe", "CS", "4.0")

print(student1.name)