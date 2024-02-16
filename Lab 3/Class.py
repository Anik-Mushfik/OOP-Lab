class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} => {self.grade}"
    
    def __del__(self):
        print("Deleted!")
    
p_1 = Student("Musfique", "A")
print(p_1)
del p_1