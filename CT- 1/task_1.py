class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.trimester = []

    def add_course(self, course):
        if course not in self.trimester:
            self.trimester.append(course)
        else:
            print(f"Course already exists!")

    def remove_course(self, course):
        if course in self.trimester:
            self.trimester.remove(course)
        else:
            print(f"Course doesn't exists!!!")
    
    def calculate_payment(self):
        total_payment = 0
        for course in self.trimester:
            total_payment += (course.credit_hour * 5000)
        print(f"Total Payment: {total_payment}")


class Courses:
    def __init__(self, name, credit_hour, gpa = 0.0):
        self.name = name
        self.gpa = gpa
        self.credit_hour = credit_hour

    def __str__(self):
        return f"Course name: {self.name}; GPA: {self.gpa}; Credit Hour: {self.credit_hour}"
    

stu_1 = Student("Musfique", "0152330101")

course_1 = Courses("BDS", 3, 4.00)
print(course_1)
stu_1.add_course(course_1)

course_2 = Courses("OOP", 3, 4.00)
print(course_2)
stu_1.add_course(course_2)

course_3 = Courses("English", 2, 4.00)
print(course_3)
stu_1.add_course(course_3)

stu_1.calculate_payment()


