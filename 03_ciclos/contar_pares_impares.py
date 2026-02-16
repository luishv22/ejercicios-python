#Programa que recibe 5 números 
#y regresa dos valores: pares e impares

def contar_pares_impares():
    numeros = []
    pares =  0
    impares = 0

    # pedir 5 números
    for i in range(5):
        num = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)

    # contar pares e impares
    for n in numeros:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return pares, impares

# programa principal
pares, impares = contar_pares_impares()

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
