
def validation_name():
    item = input('Enter your name: ')
    if item.isdigit():
        raise ValueError("The name cannot be a number")   
    else:
        return item

def validation_age():
    item = (input('Enter your age: '))
    if not item.isdigit():
        raise ValueError("Invalid number")
    else:
        return int(item)


try:
    valid_name = validation_name()
    valid_age = validation_age()
    print(f'Hello {valid_name}, your age is {valid_age} years old')
except ValueError as err:
    print(f'Error {err}')






