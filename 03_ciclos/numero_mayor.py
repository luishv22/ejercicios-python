#Programa que recibe 5 números
#y regresa el mayor

def obtener_mayor():
    numeros = []

    # pedir 5 números
    for i in range (5):
        num = int(input(f"Ingrese el número {i +1}: "))
        numeros.append(num)

    # encontrar el número mayor
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    
    return mayor

resultado = obtener_mayor() 
print(f"El número mayor es: {resultado}")
