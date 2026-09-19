class   Rectangle:
    def __init__(self, width, height):
        
        if width <= 0 or height <= 0:
                raise ValueError('Width and height has to be positive')
        self.width = width
        self.height = height
        
        print('Ingrese valores mayores a 0')


    def get_area(self):
       return self.width * self.height 

    def get_perimeter(self):
        return (self.width)*2 + (self.height)*2 

try:
    my_rectangle = Rectangle(10,-10)
    print(f'The area is {my_rectangle.get_area()}')
    print(f'The perimeter is {my_rectangle.get_perimeter()}')   
except ValueError as error:
    print(error)