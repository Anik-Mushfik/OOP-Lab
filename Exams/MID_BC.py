from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
         print("Make Sound")

    @abstractmethod
    def move(self):
        print("The animal is flying")



class Mammal(Animal):
    def __init__(self, name:str, age:int, fru_colour:str):
        super().__init__(name, age)
        self.fur_colour = fru_colour

    def give_birth(self):
        print(f"{self.name} mammle is giving birth!")

    def make_sound(self):
        print(f"{self.name} mammle is making sound!")

    def move(self):
        print(f"{self.name} mammle is swimming.")


class Bird(Animal):
    def __init__(self, name:str, age:int, wing_span:float):
        super().__inir__(name, age)
        self.wing_spam = wing_span

    def fly(self):
        print(f"{self.name} bird is flying!")

    def make_sounf(self):
        print(f"{self.name} bird id making sound.")

    def move(self):
        print(f"{self.name} bird moves by flying.")


class Reptile(Animal):
    def __init__(self, name:str, age:int, scale_colour:str):
        super().__init__(name, age)
        self.scale_colour = scale_colour

    def shed_skin(self):
        print(f"{self.name} reptile is shedding it's skin!")

    def make_sound(self):
        print(f"{self.name} reptile is making sound now!")

    def move(self):
        print(f"{self.name} reptile is moving on it's feet.")



class Lion(Mammal):
    def __init__(self, name:str, age:int, fru_colour:str, mane_color:str):
        super().__init__(name, age, fru_colour)
        self.mane_color = mane_color
        print(f"The mane color of {self.name} lion is {self.mane_color}.")


class Eagle(Bird):
    def __init__(self, name:str, age:int, wing_span:float, beak_length:float):
        super().__init__(name, age, wing_span)
        self.beak_length = beak_length
        print(f"The beak length of {self.name} eagle is {self.beak_length} cm.")


class Snake(Reptile):
    def __init__(self, name:str, age:int, scale_colour:str, venomous:bool):
        super().__init__(name, age, scale_colour)
        self.venomous = venomous
        if venomous:
            print(f"{self.name} snake is venomous.")
        else:
            print(f"{self.name} snake is not venomous.")


