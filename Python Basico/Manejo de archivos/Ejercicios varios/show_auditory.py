def show_auditory(route):
    print("\n   --- Leyendo registros    desde el   disco---")
    with open(route, 'r', encoding='utf-8') as file:
        lines = file.readlines()


        for indice, line in enumerate(lines, start=1):
            print(f'Renglon { indice} : {line.strip()}')


show_auditory('bitacora.txt')     