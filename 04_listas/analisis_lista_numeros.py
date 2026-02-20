# Programa que solicita números al usuario hasta que escriba "salir"
# luego calcular:
# - Promedio
# - Número mayor
# - Número menor 
# usando listas y ciclos.

def lista_promedio():    
    
    # lista para almacenar los números ingresados
    numeros = []

    # bucle infinito hasta que el usuario escriba "salir"
    while True:
        entrada = input("Ingresa un número o escribe 'salir': ")

        # condición para terminar la captura
        if entrada == "salir":
            break
        
        # conversión de la entrada a entero  y almacenamiento en la lista
        num = int(entrada)
        numeros.append(num)
    
    # verificar que la lista no esté vacía
    if numeros:

        # variables para calcular el promedio
        suma = 0
        contador = 0
        
        # recorrer la lista para sumar y contar elementos
        for n in numeros:
            suma += n
            contador += 1

        # calcular promedio
        promedio = suma / contador
        print(f"El promedio es: {promedio}")

        # inicializar mayor y menor con el primer elemento
        mayor = numeros[0]
        menor = numeros[0]

        for a in numeros:
            if a > mayor:
                    mayor = a
            if a < menor:
                    menor = a

        print(f"Número mayor: {mayor}")
        print(f"Número menor: {menor}")

    else:
        print("La lista esta vacía")

# llamar a la función principal
lista_promedio()
