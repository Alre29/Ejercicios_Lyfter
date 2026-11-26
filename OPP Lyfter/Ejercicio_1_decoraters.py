from functools import wraps

def log_parameters_and_returns(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling to {func.__name__}')
        print(f'-> Args like (*args) {args}')
        print(f'-> Args with key like (**Kwargs) {kwargs}')

        result = func(*args, **kwargs)

        print(f' <- retorno de  {func.__name__} :  {result} \n')

        return result
    return wrapper


@log_parameters_and_returns
def add(a,b):
    return a + b

total = add(10,35)

@log_parameters_and_returns
def create_profile(name, age, active = True):
    return (f'Usear  {name} ({age} years) - Status: {active}')

new_user = create_profile("Pepe", 30, active=False)