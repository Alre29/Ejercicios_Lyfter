my_list = []
wildcard=0


for index in range(0, 10):

    wildcard = int(input(f'Ingrese un número {index+1}: '))
    if index == 0:
        highest_number = wildcard
    my_list.append(wildcard)
    if wildcard > highest_number:
        highest_number = wildcard

    

print(f'{my_list} y el mayor es {highest_number}')