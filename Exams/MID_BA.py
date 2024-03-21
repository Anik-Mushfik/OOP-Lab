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



class Person:
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender}")


class Employee(Person):
    def __init__(self, name:str, age:int, gender:str, employee_id:str, department:str):
        super().__init__(name, age, gender)
        self.emplayee_id = employee_id
        self.department = department

    def manage_tasks(self):
        print(f"Task Managed")


class Student(Person):
    def __init__(self, name:str, age:int, gender:str, student_id:str, major:str):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def submit_assignment(self, submission_date, deadline):
        deadline = list(map(int, deadline.split("/")))
        deadline_days = (deadline[1]*30) + deadline[0]
        submission_date = list(map(int, submission_date.split("/")))
        submission_date_days = (submission_date[1]*30) + submission_date[0]

        if (submission_date_days <= deadline_days):
            print(f"Your assignment has been submited!")
        else:
            print(f"Your submission date has passed!!! \nYou are {submission_date_days - deadline_days} days late!!!")

    def __str__(self):
        return f"Student name: {self.name} \nID: {self.student_id} \nAge: {self.age} \nGender: {self.gender} \nMajor: {self.major}"
    def __repr__(self):
        return f"Student name: {self.name}; ID: {self.student_id}"


class Admin(Employee):
    def __init__(self, employee_id:str, department:str, name:str, age:int, gender:str, admin_id:str):
        super().__init__(employee_id, department, name, age, gender)
        self.admin_id = admin_id

    def handle_requests(n):
        print(f"{n} requests handled.")


class Teacher(Employee):
    def __init__(self, name:str, age:int, gender:str, employee_id:str, department:str, teacher_id:str, designation:str, subject_taught:str):
        super().__init__( name, age, gender, employee_id, department)
        self.teacher_id = teacher_id
        self.designation = designation
        self.subject_taught = subject_taught

    def conduct_class(self):
        print(f"{self.designation} {self.name} is teaching {self.subject_taught}.")

    def __str__(self): 
        return f"Teacher name: {self.name} \nID: {self.teacher_id} \nAge: {self.age} \nGender: {self.gender} \nEmplyee ID: {self.emplayee_id} \nDepartment: {self.department} \nDesignation: {self.designation} \nSubject taught: {self.subject_taught}"

    def __repr__(self):
        return f"Teacher name: {self.name}; ID: {self.teacher_id}; Designation: {self.designation}; Department: {self.department}; Subject: {self.subject_taught}"


class Classroom:
    #def __init__(self, teacher:Teacher, *students:Student):
        #self.teacher = teacher
        #self.students = [stu for stu in students]
    def __init__(self):
        self.teacher = None
        self.students = []

    def display_class_info(self):
        print(f"Teacher Info: \n{self.teacher}")
        print(f"\nStudents Info:")
        #print(self.students)
        for i in range(len(self.students)):
            print(f"{i+1}. {self.students[i]}")
        

    def add_teacher(self, teacher:Teacher):
        self.teacher = teacher

    def add_student(self, student:Student):
        self.students.append(student)

    def conduct_class_session(self):
        for stu in self.students:
            if stu == self.students[-1]:
                print(stu.name, end=" ")
            else:
                print(stu.name, end=", ")
        print(f"are attending the OOP class being taken by {self.teacher.designation} {self.teacher.name}.")
    
    #def conduct_class_session(self):
        #print(*self.students, sep="\n\n")
        #print(f"are attending the OOP class being taken by {self.teacher.designation} {self.teacher.name}")



class_1 = Classroom()
t_1 = Teacher("DMF", 46, "Male", "39874", "Data Science", "193479", "Professor", "Machine Learning")
class_1.add_teacher(t_1)

s_1 = Student("Musfique", 21, "Male", "0152330101", "Data Science")
s_2 = Student("Tasfiya", 21, "Female", "0152330116", "Data Science")
class_1.add_student(s_1)
class_1.add_student(s_2)

class_1.display_class_info()
class_1.conduct_class_session()
