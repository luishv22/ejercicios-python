# Programa que guarda la información de un estudiante en un archivo JSON
# y luego la lee para mostrarla en pantalla.

import json

# Diccionario con datos del estudiante
estudiante = {
    "nombre": "Luis",
    "edad": 23,
    "carrera": "Ingenieria en sistemas computacionales"
}

# Guardar datos en archivo JSON
with open("estudiante.json", "w") as archivo:
    json.dump(estudiante, archivo, indent=4)

# Leer datos desde el archivo JSON
with open("estudiante.json", "r") as archivo:
    datos = json.load(archivo)

# Mostrar información cargada
print(datos)
print(datos["nombre"])
