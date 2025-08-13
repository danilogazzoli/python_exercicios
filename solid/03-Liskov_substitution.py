# Subtypes must be substitutable for their base types.
# For example, if you have a piece of code that works with a Shape class, 
# then you should be able to substitute that class with any of its subclasses, such as Circle or Rectangle, without breaking the code.


#Implementação que viola este princípio
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value    


square = Square(5)
print(vars(square))
#{'width': 5, 'height': 5}

square.width = 7
print(vars(square))
#{'width': 7, 'height': 7}

square.height = 9
print(vars(square))
#{'width': 9, 'height': 9}            


# Implementação em conformidade:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

get_total_area([Rectangle(10, 5), Square(5)])    

#Here, you pass a pair consisting of a rectangle and a square into a function that calculates their total area. 
# Because the function only cares about the .calculate_area() method, it doesn’t matter that the shapes are different. 
# This is the essence of the Liskov substitution principle.