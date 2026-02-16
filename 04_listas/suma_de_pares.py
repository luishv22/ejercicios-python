# Programa que recibe una lista, suma solo los números pares
# y regresa el resultado

def suma_de_pares(lista):
    suma = 0 

    for numero in lista:
        if numero % 2 == 0:
            suma += numero 

    return suma

# Programa principal
entrada = input("Ingresar los números separados por espacio: ")
numeros = list(map(int,entrada.split()))

resultado = suma_de_pares(numeros)
print(f"El resultado es: {resultado}")
