class User:
    def __init__(self, first_name, last_name, age, income):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.income = income

    def getFullName(self):
        return f"{self.first_name} {self.last_name}"
    
    def show(self):
        print(f"This is {self.getFullName()}")
        print(f"He/She is {self.age} years old.")
        print(f"His/Her income is {self.income} BDT.")

    def __str__(self):
        """It will always return a string.
        __str__ method is used to describe the object."""
        return f"Name: {self.getFullName()}\nAge: {self.age}\nIncome: {self.income}"
    
    def __del__(self):
        print("bye")

user_1 = User("Jhon", "Maxwell", 54, 16000)
user_1.show()
print(user_1)
del user_1
print(user_1)