
import os
def ask_root():
    while True:
        root = input('Introduce el nombre del archivo con su extension: ')

        if os.path.exists(root):
            return root
        else:
            print(f'El archivo no existe en esa carpeta')

def ask_final_location():
    root = input('Introduce el nombre para el NUEVO archivo ordenado con su extensión:, por ejemplo "archivo.txt": ')
    return root


def read_songs(messy_list):
    with open(messy_list, 'r', encoding='utf-8') as songs:
        list_songs = songs.readlines()
    print(f'Estas son las listas cargadas {list_songs}')
    return list_songs


def sort_songs(songs):
    ordered_songs = sorted(songs)
    print(f'Estas son las listas ordenadas{ordered_songs}')
    return ordered_songs


def write_songs(songs, new_list):
    with open(new_list, 'w', encoding='utf-8') as ordered_songs:
        ordered_songs.writelines(songs)
    print('Canciones escritas')

file = ask_root()
read_file = read_songs(file)
sorted_file = sort_songs(read_file)
final_file = ask_final_location()
write_songs(sorted_file, final_file)