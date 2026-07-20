def inicialing_bitacora(route):
    with open(route, 'w', encoding='utf-8') as file:
        file.write("==Bitacora System - Starting==\n")
        file.write("Registro automatizado de eventos. \n")
    print(f"Archivo '{route}' inicializado con exito")

inicialing_bitacora('bitacora.txt')

