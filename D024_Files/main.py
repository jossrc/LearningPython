# LEER ARCHIVO

"""
    FORMA 01 :
      Para leer un archivo se debe seguir una secuencia de pasos:
        1. Abrir el archivo  : Uso de la función open().
        2. Leer el archivo   : Uso del método read().
        3. Cerrar el archivo : Uso del método close().
"""

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

"""
    FORMA 02 :
      Se usa el `with` para evitar el
      uso método close() que libera memoria.
      Los pasos 1 y 2 son necesarios.
"""


with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# ESCRIBIR ARCHIVO

"""
    El método open() tiene un segundo parámetro (mode)
    este permite el tipo de uso que le daremos al archivo.
    Por defecto el `mode` es "r" (Read)
      * "w" (Write)  : Borra todo el contenido y lo suplanta con el nuevo
      * "a" (Append) : Permite agregar más contenido al archivo existente.

    Para escribir un archivo se usa el método write()
    Si el archivo no existe, crea y lo escribe
"""

with open("my_file.txt", mode="a") as file:
    file.write("\nNew paragraph")
