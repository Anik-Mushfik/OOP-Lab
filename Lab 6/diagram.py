"""
If green : 2*height*base
Else if red : 1.5*height*base
Else : whatever remains in the super class
"""

class Triangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base

    def getArea(self):
        return .5*self.height*self.base
    

class ColoredTriangle(Triangle):
    def __init__(self, height, base, colour):
        super().__init__(height, base)
        self.colour = colour.title()

    def getArea(self):
        if self.colour == "Green":
            return 2*self.height*self.base
        elif self.colour == "Red":
            return 1.5*self.height*self.base
        else:
            return super().getArea()

    
t_1 = Triangle(10,5)
print(t_1.getArea())

ct_1 = ColoredTriangle(5,10, "green")
print(ct_1.colour)
print(ct_1.getArea())

ct_1 = ColoredTriangle(5,10, "Red")
print(ct_1.colour)
print(ct_1.getArea())

ct_1 = ColoredTriangle(5,10, "Yellow")
print(ct_1.colour)
print(ct_1.getArea())