def write_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

new_text = "Capítulo II. Que trata de la primera salida que de su tierra hizo el ingenioso Don Quijote."

write_new_file('quijote_capitulo2.txt', new_text)



