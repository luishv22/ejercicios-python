# Programa que recibe una lista 
# y regresa cuántos números son mayores a 10

def numeros_mayores(lista):
    mayores = 0

    
    for n in numeros:
        if n > 10:
            mayores += 1

    return mayores

# Programa principal
numeros = []

for i in range(5):
    num = int(input(f"Ingrese el número {i +1}: "))
    numeros.append(num)

resultado = numeros_mayores(numeros)
print(f"Números mayores: {resultado}")
