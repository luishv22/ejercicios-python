import json

# Función principal del menú
def menu_principal():
    
    # Verificar si ya hay un archivo guardado para cargarlo
    try:
        with open("estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo)

    # Si no existe ningún archivo guarda uno nuevo       
    except FileNotFoundError:

        # Lista de estudiantes
        estudiantes = [
            {
                "nombre": "Axel",
                "edad": 25,
                "carrera": "Ingenieria Industrial"
            },
            {
                "nombre": "Daniel",
                "edad": 23,
                "carrera": "Ingenieria en Software"
            },
            {
                "nombre": "Berenice",
                "edad": 19,
                "carrera": "Licenciatura en Gastronomia"
            },
            {
                "nombre": "Julio",
                "edad": 20,
                "carrera": "Ingenieria Civil"
            }
        ]

        # Guardar datos en archivo JSON
        with open("estudiantes.json", "w") as archivo:
            json.dump(estudiantes, archivo, indent=4)

    # Bucle principal del menú
    while True:
        print("\n--- Gestión de estudiantes ---")
        print("1. Mostrar todos los estudiantes")
        print("2. Agregar un estudiante")
        print("3. Eliminar un estudiante por nombre")
        print("4. Modificar un estudiante")
        print("5. Salir")
        # Solicitar opción
        opcion = input("Elige una opción: ")

        # Opción 1: Mostrar lista de estudiantes
        if opcion == "1":
            print("\n--- Lista de estudiantes ---")
            # Ciclo que recorre cada diccionario y muestra los datos de cada estudiante
            for estudiante in estudiantes: 
                print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Carrera: {estudiante['carrera']}")
        # Opción 2: Agregar un estudiante nuevo        
        elif opcion == "2":
            # Bucle para guardar los datos en un nuevo diccionario
            while True:
                # Verificar que los datos ingresados sean los correctos
                try:
                    print("\n--- Ingrese los datos del estudiante que desea guardar ---")
                    nombre = input("Ingrese el nombre: ")
                    edad = int(input("Ingrese la edad: "))
                    carrera =input("Ingrese la carrera: ")
                    
                    # Guardar los datos en un nuevo diccionario
                    estudiantes.append({
                        "nombre": nombre, 
                        "edad": edad, 
                        "carrera": carrera
                        })
                    # Actualiza el archivo agregando el nuevo estudiante
                    with open("estudiantes.json", "w") as archivo:
                        json.dump(estudiantes, archivo, indent=4)

                    print("Estudiante agregado correctamente")
                    entrada = input("Si desea guardar otro estudiante continue (o escribe 'salir' para volver al menú): ")
                    # Salida del bucle 
                    if entrada.lower() == 'salir':
                        break

                except ValueError:
                    print("Entrada inválida, intenta de nuevo")
        # Opción 3: Eliminar estudiante
        elif opcion == "3":
            eliminar = input("Ingrese el nombre del estudiante que quiere eliminar: ")
            encontrado = False
            # Ciclo para buscar al estudiante por nombre
            for estudiante in estudiantes[:]:
                if estudiante["nombre"].lower() == eliminar.lower():
                    # Eliminar al estudiante encontrado
                    estudiantes.remove(estudiante)
                    encontrado = True
                    print("Estudiante eliminado")
                    # Actualiza el archivo eliminando los datos del estudiante
                    with open("estudiantes.json", "w") as archivo:
                        json.dump(estudiantes, archivo,indent=4)

            if not encontrado:
                print("Estudiante no encontrado")

        # Opción 4: Modificar estudiante
        elif opcion == "4":
            modificar = input("Ingrese el nombre del estudiante que quiere modificar: ")
            encontrado = False
            # Ciclo para buscar al estudiante por nombre
            for estudiante in estudiantes:
                if estudiante["nombre"].lower() == modificar.lower():
                    encontrado = True
                    # Menú para modificar los datos del estudiante encontrado
                    print("¿Que deseas modificar?: ")
                    print("1. Nombre")
                    print("2. Edad")
                    print("3. Carrera")
                    # Solicitar opción 
                    opcion_mod = input("Elija una opción: ")

                    # Opción 1: Modificar nombre
                    if opcion_mod == "1":
                        nuevo = input("Ingrese el nuevo nombre: ")
                        # Aplicar la modificación de nombre
                        estudiante["nombre"] = nuevo

                    # Opción 2: Modificar edad
                    elif opcion_mod == "2":
                        # Verificar que se ingrese el dato solicitado
                        try:
                            nuevo = int(input("Ingrese la nueva edad: "))
                            # Aplicar la modificación de edad
                            estudiante["edad"] = nuevo
                        except ValueError:
                            print("Edad inválida")
                            continue
                    
                    # Opción 3: Modificar carrera
                    elif opcion_mod == "3":
                        nuevo = input("Ingrese la nueva carrera: ")
                        # Aplicar la modificación de carrera
                        estudiante["carrera"] = nuevo

                    else:
                        print("Opción inválida, intenta de nuevo")
                        break

                    # Guardar el archivo con los datos del estudiante modificado
                    with open("estudiantes.json", "w") as archivo:
                        json.dump(estudiantes, archivo,indent=4)

                    print("Cambios realizados correctamente")
                    break
            
            if not encontrado:
                print("Estudiante no encontrado")
        # Opción 5: Salir del programa
        elif opcion == "5":
            print("Saliendo del programa. . . .")
            break

        else:
            print("Opción inválida, intenta de nuevo")
# Llamar a la función principal
menu_principal()
