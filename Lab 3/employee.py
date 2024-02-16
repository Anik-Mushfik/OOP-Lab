"""Employee management system
Attributes:
- Name
- Age
- Salary (private)
- Joining date

Methods:
- giveBonus (age>30 = salary 3% increment)
- getSalary ()

"""

class Employee:
    def __init__(self, name, age, salary, joining_date):
        self.name = name
        self.age = age
        self.__salary = salary
        self.joining_date = joining_date

    def giveBonus(self):
        if (self.age > 30):
            self.__salary += (self.__salary * 0.03)

    def getSalary(self):
        return self.__salary
    
