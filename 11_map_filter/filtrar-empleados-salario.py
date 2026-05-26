# Filtra empleados con salario mayor a 10000
# Convierte sus nombres a mayúsculas

# Lista original de empleados con nombre y salario
empleados = [
    {"nombre": "Ana",   "salario": 12000},
    {"nombre": "Luis",  "salario": 8500},
    {"nombre": "María", "salario": 15000},
    {"nombre": "Pedro", "salario": 7000},
    {"nombre": "Sofía", "salario": 11000},
]

# Crear una nueva lista con los nombres en mayúsculas
# de los empleados que ganan más de 10000
salario_mayor= list(
    map(
        # Convertir el nombre del empleado a mayúsculas 
        lambda nom: nom['nombre'].upper(),

        # Filtrar empleados con salario mayor a 10000
        filter(lambda emp: emp['salario'] > 10000, empleados)
    )
)

# Mostrar la lista final
print(salario_mayor  )
