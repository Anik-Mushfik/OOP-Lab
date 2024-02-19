class Pet:
    def __init__(self, name, type, hunger_level=0, happiness_level=100):
        self.name = name
        self.type = type
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level

    def __str__(self):
        return f"Pet name: {self.name}; Pet type: {self.type}; Hungry: {self.hunger_level}%; Happiness: {self.happiness_level}%"
    
class Owner:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name} is the owner of {self.pet.name}"
    
    def feed_pet(self):
        if (self.pet.hunger_level >= 20):
            self.pet.hunger_level -= 20
        else:
            self.pet.hunger_level = 0
    
    def play_with_pet(self):
        if (self.pet.happiness_level <= 65):
            self.pet.happiness_level += 35
        else:
            self.pet.happiness_level = 100

milo = Pet("Milo", "Cat",77, 50)
anik = Owner("Anik", milo)
print(milo)
anik.feed_pet()
anik.play_with_pet()

print(milo)
print(anik)