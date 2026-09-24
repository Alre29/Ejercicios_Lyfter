
class Person:

    def __init__(self, id_person):
        self.id_person = id_person


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def get_in_the_bus(self, person):
        if len(self.passengers)< self.max_passengers:
            self.passengers.append(person)
            print(f'The person with ID {person.id_person} is in the bus now')
        else:
            print(f'The bus is full. The person with ID{person.id_person} cannot  get in') 

    def get_out_the_bus(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'Bye bye! Person with id {person. id_person}')
        else:
            print(f'Is not  on the bus')

my_bus = Bus(4)            

p1 = Person("D-01")
p2 = Person("D-02")
p3 = Person("D-03")
p4 = Person("D-04")

my_bus.get_in_the_bus(p1)
my_bus.get_in_the_bus(p2)
my_bus.get_in_the_bus(p3)

my_bus.get_out_the_bus(p2)

my_bus.get_in_the_bus(p4)

print("\n Passengers in the bus right now are :")

for passenger in my_bus.passengers:
    print(passenger.id_person)



