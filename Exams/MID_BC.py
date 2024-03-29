from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass



class Mammal(Animal):
    def __init__(self, name:str, age:int, fru_colour:str):
        super().__init__(name, age)
        self.fur_colour = fru_colour

    # def give_birth(self):
    #     print(f"{self.name} mammle is giving birth!")

    # def make_sound(self):
    #     print(f"{self.name} mammle is making sound!")

    # def move(self):
    #     print(f"{self.name} mammle is swimming.")


class Bird(Animal):
    def __init__(self, name:str, age:int, wing_span:float):
        super().__init__(name, age)
        self.wing_spam = wing_span

    def make_sound(self):
        raise NotImplementedError("Subclasses must implemente makes_sound()")

    def move(self):
        raise NotImplementedError("Subclasses must implemente move()")

    # def fly(self):
    #     print(f"{self.name} bird is flying!")

    # def make_sound(self):
    #     print(f"{self.name} bird id making sound.")

    # def move(self):
    #     print(f"{self.name} bird moves by flying.")


class Reptile(Animal):
    def __init__(self, name:str, age:int, scale_colour:str):
        super().__init__(name, age)
        self.scale_colour = scale_colour

    # def shed_skin(self):
    #     print(f"{self.name} reptile is shedding it's skin!")

    # def make_sound(self):
    #     print(f"{self.name} reptile is making sound now!")

    # def move(self):
    #     print(f"{self.name} reptile is moving on it's feet.")



class Lion(Mammal):
    def __init__(self, name:str, age:int, fru_colour:str, mane_color:str):
        super().__init__(name, age, fru_colour)
        self.mane_color = mane_color
        print(f"The mane color of {self.name} lion is {self.mane_color}.")
    
    def give_birth(self):
        print(f"{self.name} mammle is giving birth!")

    def make_sound(self):
        print(f"{self.name} mammle is making sound!")

    def move(self):
        print(f"{self.name} mammle is swimming.")



class Eagle(Bird):
    def __init__(self, name:str, age:int, wing_span:float, beak_length:float):
        super().__init__(name, age, wing_span)
        self.beak_length = beak_length
        print(f"The beak length of {self.name} eagle is {self.beak_length} cm.")

    def fly(self):
        print(f"{self.name} bird is flying!")

    def make_sound(self):
        print(f"{self.name} bird id making sound.")

    def move(self):
        print(f"{self.name} bird moves by flying.")


class Snake(Reptile):
    def __init__(self, name:str, age:int, scale_colour:str, venomous:bool):
        super().__init__(name, age, scale_colour)
        self.venomous = venomous

    def is_venomous(self):
        if self.venomous:
            print(f"{self.name} snake is venomous.")
        else:
            print(f"{self.name} snake is not venomous.")

    def shed_skin(self):
        print(f"{self.name} reptile is shedding it's skin!")

    def make_sound(self):
        print(f"{self.name} reptile is making sound now!")

    def move(self):
        print(f"{self.name} reptile is moving on it's feet.")



l_1 = Lion("Shingho", 23, "Lil", "Kala")
s_1 = Snake("Ojogor", 12, "lil", True)
b_1 = Eagle("igol", 23, 4.5, 12)

l_1.make_sound()
s_1.make_sound()
b_1.make_sound()

l_1.give_birth()
b_1.fly()
s_1.move()
s_1.is_venomous()

hi = Bird("afd", 13, 34.6)
hi.make_sound()