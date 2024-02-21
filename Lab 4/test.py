class Course:
    def __init__(self, name, credit_hour):
        self.name = name
        self.credit_hour = credit_hour
        self.gpa = 0.00

course_1 = Course()


##
lst = [5,1,4,1,1,6]
lst.remove(1)
print(lst)

class Course:
    def __init__(self, name, credit_hour):
        self.name = name
        self.gpa = 0.00
        self.credit_hour = credit_hour

    def __str__(self):
        return f"Course name: {self.name}; GPA: {self.gpa}; Credit hour: {self.credit_hour}"


course_1 = Course("OOP", 3)
print(course_1)