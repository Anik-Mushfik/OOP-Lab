class Employee:
    def __init__(self, name, age, salary, joining_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.joining_date = joining_date
    
    def show(self):
        print(f"Name: {self.name} \n\tAge: {self.age} \n\tSalary: {self.salary} \n\tJoining Date: {self.joining_date}")

    def insertEmployee(self, filename):
        with open(filename, "a") as file:
            new_emp = f"\n{self.name}, {self.age}, {self.salary}, {self.joining_date}"
            file.write(new_emp)

emp_1 = Employee("Anik", 23, 15000, "25 January, 2001")
emp_2 = Employee("Musfique", 19, 11000, "31 February, 2023")
emp_3 = Employee("Ahmed", 28, 60000, "15 March, 1995")
emp_4 = Employee("Hoq Maola", 15, 34000, "9 December, 2005")


emp_1.show()
emp_2.show()
emp_3.show()
emp_4.show()


emp_1.insertEmployee("D:\Musfique - 0152330101\lab_2\employee_data\emplyee.txt")
emp_2.insertEmployee("D:\Musfique - 0152330101\lab_2\employee_data\emplyee.txt")
emp_3.insertEmployee("D:\Musfique - 0152330101\lab_2\employee_data\emplyee.txt")
emp_4.insertEmployee("D:\Musfique - 0152330101\lab_2\employee_data\emplyee.txt")