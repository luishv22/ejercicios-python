# Sistema de menú que permite:
# - agregar números 
# - mostrar lista
# - calcular promedio
# - obtener mayor y menor
# - contar pares e impares
# - limpiar la lista
# Utiliza funciones, listas y estructuras de control.

# -------------------------------------------------------------
# Calcular el promedio de una lista de números
# -------------------------------------------------------------
def calcular_promedio(lista):
    # verificar que la lista no esté vacía
    if not lista:
        return 0

    suma = 0
    # recorrer la lista y acumular la suma
    for n in lista:
        suma += n
    # calcular promedio
    promedio = suma / len(lista)
    return promedio

# -------------------------------------------------------------
# Obtener el número mayor de la lista
# -------------------------------------------------------------
def obtener_mayor(lista):
    # verificar que la lista no esté vacía
    if not lista:
        return 0
    # suponer que el primero es el mayor
    mayor = lista[0]
    # comparar desde el segundo número
    for n in lista[1:]: 
        if n > mayor:
            mayor = n

    return mayor

# -------------------------------------------------------------
# Obtener el número menor de la lista
# -------------------------------------------------------------
def obtener_menor(lista):
    # verificar que la lista no esté vacía
    if not lista:
        return 0
    # suponer que el primero es el menor
    menor = lista[0]

    # comparar desde el segundo número
    for n in lista[1:]: 
        if n < menor:
            menor = n

    return menor

# -------------------------------------------------------------
# Contar cuántos números pares e impares hay
# -------------------------------------------------------------
def contar_pares_impares(lista):
    # verificar que la lista no esté vacía
    if not lista:
        return 0, 0

    pares = 0
    impares = 0
    # recorrer la lista y clasificar
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

# -------------------------------------------------------------
# Guardar los datos en un archivo
# -------------------------------------------------------------
def guardar_archivo(lista, nombre_archivo="numeros.txt"):
    try:
        with open(nombre_archivo, "w") as archivo:
            for n in lista:
                archivo.write(str(n) + "\n")
        return True

    except Exception:
        return False

# -------------------------------------------------------------
# Cargar los datos de un archivo
# -------------------------------------------------------------
def cargar_archivo(nombre_archivo="numeros.txt"):
    numeros = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                numeros.append(int(linea.strip()))
        return numeros

    except Exception:
        return []

# =============================================================
# FUNCIÓN PRINCIPAL (menú del sistema)
# =============================================================
def mini_sistema():
    # lista donde se almacenan los números del usuario
    numeros = []
    
    # bucle principal del menú
    while True:
        print("\n---- MENÚ ---")
        print("1. Agregar número")
        print("2. Mostrar números")
        print("3. Mostrar promedio")
        print("4. Mostrar mayor")
        print("5. Mostrar menor")
        print("6. Contar pares e impares")
        print("7. Limpiar lista")
        print("8. Guardar en archivo")
        print("9. Cargar desde archivo")
        print("10. Salir")
        # solicitar opción 
        opcion = input("Elige una opción: ")

        # -------------------------------------------------------------
        # OPCIÓN 1: Agregar números
        # -------------------------------------------------------------
        if opcion == "1":
            while True:
                try:
                    entrada = input("Ingresa un número (o escribe 'salir' para volver al menú): ")

                    if entrada.lower() == 'salir':
                        break

                    num = int(entrada)
                    numeros.append(num)
                    print("Número agregado correctamente")
                except ValueError:
                    print("Entrada inválida, intenta de nuevo")

        # -------------------------------------------------------------
        # OPCIÓN 2: Mostrar lista
        # -------------------------------------------------------------
        elif opcion == "2":
            if not numeros:
                print("La lista está vacía")
                continue

            print(f"Los números son: {numeros}")
        
        # -------------------------------------------------------------
        # OPCIÓN 3: Mostrar promedio
        # -------------------------------------------------------------
        elif opcion == "3":
            if not numeros:
                print("La lista está vacía")
                continue

            promedio = calcular_promedio(numeros)
            print(f"El promedio es: {promedio}")

        # -------------------------------------------------------------
        # OPCIÓN 4: Mostrar mayor
        # -------------------------------------------------------------
        elif opcion == "4":
            if not numeros:
                print("La lista está vacía")
                continue

            mayor = obtener_mayor(numeros)
            print(f"El número mayor es: {mayor}")

        # -------------------------------------------------------------
        # OPCIÓN 5: Mostrar menor
        # -------------------------------------------------------------
        elif opcion == "5":
            if not numeros:
                print("La lista está vacía")
                continue

            menor = obtener_menor(numeros)
            print(f"El número menor es: {menor}")

        # -------------------------------------------------------------
        # OPCIÓN 6: Contar pares e impares
        # -------------------------------------------------------------
        elif opcion == "6":
            if not numeros:
                print("La lista está vacía")
                continue

            pares , impares = contar_pares_impares(numeros)
            
            print(f"Números pares: {pares}")
            print(f"Números impares: {impares}")

        # -------------------------------------------------------------
        # OPCIÓN 7: Limpiar lista
        # -------------------------------------------------------------
        elif opcion == "7":
            numeros.clear()
            print("Lista limpiada correctamente")

        # -------------------------------------------------------------
        # OPCIÓN 8: Guardar datos en archivo
        # -------------------------------------------------------------
        elif opcion == "8":
            if not numeros:
                print("La lista está vacía, no hay nada que guardar")
                continue

            if guardar_archivo(numeros):
                print("Datos guardados correctamente")
            else:
                print("Error al guardar el archivo")

        # -------------------------------------------------------------
        # OPCIÓN 9: Cargar datos de archivo
        # -------------------------------------------------------------
        elif opcion == "9":
            datos = cargar_archivo()

            if not datos:
                print("No se pudieron cargar datos o el archivo está vacío")

            else:
                numeros = datos
                print("Datos cargados correctamente")

        # -------------------------------------------------------------
        # OPCIÓN 10: Salir
        # -------------------------------------------------------------
        elif opcion == "10":
            print("Saliendo del programa. . . . ")
            break

        # -------------------------------------------------------------
        # Opción inválida
        # -------------------------------------------------------------
        else:
            print("Opción inválida")

# llamar a la función principal
mini_sistema()
