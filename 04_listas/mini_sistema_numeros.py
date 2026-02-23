# Programa con menú interactivo que permite al usuario:
# - Agregar números a la lista 
# - Mostrar la lista
# - Calcular promedio
# - Obtener número mayor y menor

def mini_sistema():
    # lista para almacenar los números ingresados
    numeros = []

    # bucle principal del menú (se repite hasta que el usuario salga)
    while True:
        print("\n---MENÚ---")
        print("1. Agregar número")
        print("2. Mostrar números")
        print("3. Mostar promedio")
        print("4. Mostrar mayor")
        print("5. Mostrar menor")
        print("6. Salir")
        
        # solicitar opción al usuario
        opcion = input("Elige una opción: ")
        
        # ----------------------------------------------------
        # OPCIÓN 1: Agregar números a la lista
        # ----------------------------------------------------
        if opcion == "1":
            while True:
                try:
                    entrada = input("Ingresa un número (o escribe 'salir' para volver al menú): ")
                    
                    # permite regresar al menú
                    if entrada.lower() == 'salir':
                        break

                    # convertir a entero y guardar a la lista
                    num = int(entrada)
                    numeros.append(num)
                except ValueError:
                    print("Entrada invalida, intenta de nuevo")

        # -----------------------------------------------------
        # OPCIÓN 2: Mostrar lista de números
        # -----------------------------------------------------
        elif opcion == "2":
            if numeros:
                print(f"Los números ingresados son: {numeros}")
            else:
                print("La lista esta vacia")

        # -----------------------------------------------------
        # OPCIÓN 3: Calcular promedio 
        # -----------------------------------------------------
        elif opcion == "3":
            if numeros:
                suma = 0
                contador = 0

                # recorrer la lista para sumar y contar
                for n in numeros:
                        suma += n
                        contador += 1
                    
                promedio = suma / contador 
                print(f"El promedio es: {promedio}")
            else:
                print("La lista esta vacia")

        # -----------------------------------------------------
        # OPCIÓN 4: Mostrar número mayor
        # -----------------------------------------------------
        elif opcion == "4":
            if numeros:
                mayor = numeros[0]
                for n in numeros:
                    if n > mayor:
                        mayor = n

                print(f"Número mayor: {mayor}")
            else:
                print("La lista esta vacia")

        # -----------------------------------------------------
        # OPCIÓN 5: Mostrar número menor
        # -----------------------------------------------------
        elif opcion == "5":
            if numeros:
                menor = numeros[0]
                for n in numeros:
                    if n < menor:
                        menor = n

                print(f"El número menor es: {menor}")
            else:
                print("La lista esta vacia")

        # -----------------------------------------------------
        # OPCIÓN 6: Salir del programa
        # -----------------------------------------------------
        elif opcion == "6":
            print("Saliendo del programa. . .")
            break

        # -----------------------------------------------------
        # Opción invalida
        # -----------------------------------------------------
        else:
            print("Opción invalida") 

# llamar a la función principal
mini_sistema()
