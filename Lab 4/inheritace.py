class Person:
    def __init__(self, name, birth_place):
        self.name = name
        self.birth_place = birth_place

    def display(self):
        print(f"I am {self.name} from {self.birth_place}")

class Employee(Person):
    def __init__(self):
        print("Emplyee Called")

emp_1 = Employee()
Employee.display()