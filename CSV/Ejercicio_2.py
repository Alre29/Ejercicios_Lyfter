import csv

def save_game_ranking(path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
       

        writer = csv.writer(file, delimiter='\t')

        headers = ['nombre', 'genero', 'desarrollador', 'clasificacion']

        writer.writerow(headers)

        print('---Inicio  de registro---')

        while True:
            print('\n Introduzca los siguientes datos del juego')
            name = input('Nombre: ')
            gender = input('Género: ')
            developer = input('Desarrollador: ')
            class_esrb = input('Calificación ESRB: ')

            game = [name,gender,developer,class_esrb ]

            writer.writerow(game)

            next_game = input('Desea agregar otro juego s/n: ').strip().lower()
            
            if next_game != 's':
                print('\n Datos guardados ')
                break



save_game_ranking('videogames_ranks.tsv')