my_list = ['15','pera','6.1','3','F']

def add_values(items):
    sum_values = 0
    for item in items:
        
        try:
            float_number = float(item)
            sum_values += float_number
            print (f'{float_number} Correctly added ')

        except ValueError:
            print (f'Invalid element: {item} ')

    print(f'Total sum {sum_values}')

add_values(my_list)