class SuperDad:

    def fly(self):
        return 'fly!'

class SuperMom:

    def teleport(self):
       return 'teleport'


class SuperHero:

    def __init__(self, name:str):
        self.name = name

    def get_name(self):
        return self.name

class SuperSon(SuperHero, SuperDad, SuperMom):
    pass

son = SuperSon("MovinMan")

print(f'The superhero {son.get_name()} has the power of {son.teleport()} and {son.fly()}')
