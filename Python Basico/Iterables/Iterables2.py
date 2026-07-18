my_string = 'Pizza con piña'

for index in range(len(my_string)-1,-1,-1 ): #Esta parte no me quedo muy claro el primer -1 es para indicar que se comienza del final, el segundo  no lo capto, pero el ultimo -1 indica que se va quitando 1
    print(f'{my_string[index]}')
    index =- 1