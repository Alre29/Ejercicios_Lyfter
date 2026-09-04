class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        
        return 3.1416 * (self.radius**2)

my_circle = circle(5)
print(my_circle.get_area())

    