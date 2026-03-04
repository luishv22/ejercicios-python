# Programa que guarda una lista de estudiantes en JSON,
# luego permite buscar un estudiante por nombre

import json

# Lista de estudiantes
estudiantes = [
    {
        "nombre": "Luis",
        "edad": 23,
        "carrera": "Ingenieria en sistemas"
    },
    {
        "nombre": "Carlos",
        "edad": 20,
        "carrera": "Licenciatura en contabilidad"
    },
    {
        "nombre": "Aldo",
        "edad": 25,
        "carrera": "Ingeniero bioquimico"
    }
]

# Guardar en archivo JSON
with open("estudiantes.json", "w") as archivo:
    json.dump(estudiantes, archivo, indent=4)

# Leer desde JSON
with open("estudiantes.json", "r") as archivo:
    datos = json.load(archivo)

# Solicitar nombre a buscar
buscar_nombre = input("Ingresa el nombre: ")

encontrado = False

# Buscar estudiante
for estudiante in datos:
    if estudiante["nombre"].lower() == buscar_nombre.lower():

        print("\n--- Estudiante encontrado ---")
        print(f"Nombre : {estudiante['nombre']}")
        print(f"Edad   : {estudiante['edad']}")
        print(f"Carrera: {estudiante['carrera']}")

        encontrado = True
        break

# Mostrar mensaje si no se encontró
if not encontrado:
    print("Estudiante no encontrado")
