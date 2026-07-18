import os

# Esto nos dice en qué carpeta está parado Python ahora mismo
directorio_actual = os.getcwd()
ruta_archivo = os.path.join(directorio_actual, 'mi_prueba_final.txt')

try:
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        file.write("Hola Paolo, este archivo tiene que aparecer.\n")
    print(f"✅ ¡Éxito! El archivo se creó en: {ruta_archivo}")
except Exception as e:
    print(f"❌ Hubo un error: {e}")