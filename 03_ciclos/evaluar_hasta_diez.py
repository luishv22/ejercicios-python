# Programa que pide un número y determina
# si es mayor, menor o igual a 10

def evaluar_hasta_diez():
# solicitar número al usuario
    numero = int(input("Ingresa el número: "))

    # repetir mientras el número sea diferente de 10
    while numero != 10:
    
        if numero > 10:
            print("Es mayor que diez")

        elif numero < 10:
            print("Es menor que diez")
 
        # solicitar nuevamente el número si no es 10
        numero = int(input("Ingrese el número: "))

    # mostrar mensaje cuando el número es 10
    if numero == 10:
        print("Es diez")

evaluar_hasta_diez()
