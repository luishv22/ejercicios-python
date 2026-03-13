# Programa que guarda una lista de estudiantes en un archivo JSON
# y genera un reporte con:
# - Total de estudiantes
# - Promedio de edad 
# - Estudiante mayor
# - Estudiante menor

import json

# Lista de estudiantes
estudiantes = [
    {
        "nombre": "Carlos",
        "edad": 28,
        "carrera": "Licenciatura en contabilidad"
    },
    {
        "nombre": "Luis",
        "edad": 23,
        "carrera": "Ingeniería en sistemas"
    },
    {
        "nombre": "Aldo",
        "edad": 25,
        "carrera": "Ingeniería bioquímica"
    },
    {
        "nombre": "Julio",
        "edad": 24,
        "carrera": "Licenciatura en medicina"
    }
]

# Guardar datos en archivo JSON
with open("estudiantes.json", "w") as archivo:
    json.dump(estudiantes, archivo, indent=4)

# Leer datos desde el archivo JSON
with open("estudiantes.json", "r") as archivo:
    datos = json.load(archivo)

# Calcula el total de estudiantes
def total_estudiantes(lista):
    return len(lista)

# Calcula y retorna el promedio de edad de los estudiantes
def promedio_edad(lista):
    return sum(e["edad"] for e in lista) / len(lista)

print("\n=== Reporte de Estudiantes ===")
print(f"Total de estudiantes: {total_estudiantes(datos)}")
print(f"Promedio de edad: {promedio_edad(datos):.2f}")

# Obtener el estudiante mayor y el menor
mayor = max(datos, key=lambda e: e["edad"])
menor = min(datos, key=lambda e: e["edad"])

print(f"Estudiante mayor: {mayor['nombre']}, {mayor['edad']} años")
print(f"Estudiante menor: {menor['nombre']}, {menor['edad']} años")
