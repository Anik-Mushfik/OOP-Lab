# from abc import ABC, abstractmethod
# class Person(ABC):
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def display_info(self):
#         return f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender}"
    
#     @abstractmethod
#     def random(self):
#         pass


# class Employee(Person):
#     def __init__(self,name,age,gender,employee_id, department):
#         super().__init__(name,age,gender)
#         self.employee_id = employee_id
#         self.department = department

#     def manage_task(self):
#         print(f"Tasks managed")


# class Student(Person):
#     def __init__(self,name,age,gender, student_id, major):
#         super().__init__(name,age,gender)
#         self.student_id = student_id
#         self.major = major

#     def submit_assignment(self, submission_date, deadline):
#         if submission_date <= deadline:
#             print(f"Your assingment has been submitted.")
#         else:
#             print(f"You have delaied {submission_date - deadline} days to submit the assingment!!!")

#     def random(self):
#         pass


# class Admin(Employee):
#     def __inti__(self, name,age,gender,employee_id, department, admin_id):
#         super().__init__(name,age,gender,employee_id, department)
#         self.admin_id = admin_id
        
#     def handle_request(self, n):
#         print(f"{n} requests handled")

#     def random(self):
#         pass


# class Teacher(Employee):
#     def __init__(self, name, age, gender, employee_id, department, teacher_id, designation, subject_taght):
#         super().__init__(name, age, gender, employee_id, department)
#         self.teacher_id = teacher_id
#         self.designation = designation
#         self.suject_taught = subject_taght

#     def conduct_class(self):
#         print(f"{self.designation} {self.name} is teaching {self.suject_taught}")

#     def random(self):
#         pass


# class Classroom:
#     def __init__(self):
#         self.teacher = None
#         self.students = []

#     def display_class_info(self):
#         return f"Class teacher: {self.teacher.name} \nNo of students: {len(self.students)}"
    
#     def add_teacher(self, teacher):
#         self.teacher = teacher

#     def add_student(self, student):
#         self.students.append(student)

#     def conduct_class_session(self):
#         for i in self.students:
#             if i == self.students[-1]:
#                 print(i.name, end= " ")
#             else:
#                 print(i.name, end=", ")
        
#         print(f"is attending the OOP class being taken by {self.teacher.designation} {self.teacher.name}.")


# teacher = Teacher("Swakhar" , 23, "male", 2579234, "Data Science", 23456754, "Professor", "OOP")
# teacher.conduct_class()
# stu_1 = Student("Ashik", 12, "male", 38493, "OOP")
# stu_2 = Student("Tawsif", 21, "female", 23245, "PPO")
# class_11 = Classroom()
# class_11.add_teacher(teacher)
# class_11.add_student(stu_1)
# class_11.add_student(stu_2)
# class_11.display_class_info()
# class_11.conduct_class_session()

# person = Person("abvjc", 232, "male")

# print(person.display_info())