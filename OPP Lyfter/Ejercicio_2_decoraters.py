from functools import wraps

def checker_int_or_float(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool): # este ultimo para evitar un falso positivo por el 1 o 0 del booleano
                raise TypeError(f'The Argument {arg} is not a number')

        for kwarg, value in kwargs.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f'The Argument {kwarg} = {value} is not a number')

        return func(*args,**kwargs)
    return wrapper



@checker_int_or_float
def calculate_area_rectangle(base, altura):
    return base * altura

resultado = calculate_area_rectangle(5, 5.5)
print(f'The area of rectangle is {resultado} ')



resultado = calculate_area_rectangle("p5", 5.5)
print(f'The area of rectangle is {resultado}')