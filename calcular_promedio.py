# Programa que recibe una lista de calificaciones
# y calcula el promedio 

def calcular_promedio(lista):
    suma = 0

    for numero in lista:
         suma += numero 

    promedio = suma / len(lista)
    return promedio
    
# Pedimos varias calificaciones separadas por espacio 
entrada = input("Ingresa las calificaciones separadas por espacio: ")

# Convertimos a lista de enteros
calificaciones = list(map(int,entrada.split()))
     
resultado = calcular_promedio(calificaciones)
print(f"El promedio es: {resultado}")
