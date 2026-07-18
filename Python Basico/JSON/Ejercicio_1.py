import json

def main():

    def read_pokedex(pokedex):
        with open(pokedex, 'r', encoding='utf-8') as file:
            poke_list= json.load(file)
        return poke_list

    def register_pokemon():
        print('Registra la siguiente informacion del pokemon')
        name = input('Nombre: \n')
        poke_type = input('Tipo:  \n')
        level = input('Nivel:  \n')

        pokemon = {
            "name" : name,
            "type": poke_type,
            "level": level
        }
        return pokemon

    def update_pokedex(pokedex, new_pokemon):
        with open(pokedex, 'w', encoding='utf-8') as file:
            json.dump(new_pokemon, file)
        


    pokedex = read_pokedex('pokedex.JSON')

    while True:

        new_pokemon = register_pokemon()

        pokedex.append(new_pokemon)

        update_pokedex('pokedex.JSON', pokedex)

        print('Pokemon registrado \n')
        option = input('Deseas registrar un nuevo pokemon  s/n  ').strip().lower()

        if option != 's':
            print('Desconectando pokedex')
            break



main()        