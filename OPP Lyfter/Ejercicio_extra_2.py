class Animal:

    def __init__(self, name):
        self.name = name
       

    def speak(self):
        return 'Make a sound'

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"

my_dog = Dog('Billy')
my_cat = Cat('Nala')

print(f'My dog {my_dog.name} says {my_dog.speak()}')

print(f'My Cat {my_cat.name} says {my_cat.speak()}')