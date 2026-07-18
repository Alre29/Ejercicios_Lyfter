import os

def reader_of_document(text):
    with open(text,'r', encoding='utf-8') as file:
        new_file = file.read()
    return new_file


def get_document():
    
    document = input('Introduce el nombre del archivo con su extension: ')

    if os.path.exists(document):
        return document
    else:
        print(f'El archivo no existe en esa carpeta')

def eraser(text):
    with open(text, 'r', encoding='utf-8') as file:
        new_file = file.replace('\n', ' ')
    print(f'Este es un nuevo archivo{new_file}')
    return new_file

def write(text, new_text):
    with open(text,'w', encoding='utf-8') as file:
        file.write(new_text)

    return file
