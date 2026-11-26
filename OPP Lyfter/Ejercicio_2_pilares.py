import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius:float):
        self.radius= radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius 
 
    def calculate_area(self):
        return  math.pi * (self.radius ** 2)


class Square(Shape):

    def __init__(self, side:float):
            self.side= side

    def calculate_perimeter(self):
        return self.side * 4

    def calculate_area(self):
        return self.side ** 2
    
class Rectangle(Shape):

    def __init__(self, width:float, height:float):
            self.width= width
            self.height= height

    def calculate_perimeter(self):
        return (self.width*2)+(self.height*2)

    def calculate_area(self):
        return self.height * self.width
    
my_circle = Circle(3.3)

my_square = Square(4)

my_rectangle = Rectangle(4,2)

print(f'The area of the rectangle is {my_rectangle.calculate_area()} and the perimeter is {my_rectangle.calculate_perimeter()}')


print(f'The area of the circle is {my_circle.calculate_area()} and the perimeter is {my_circle.calculate_perimeter()}')


print(f'The area of the square is {my_square.calculate_area()} and the perimeter is {my_square.calculate_perimeter()}')
