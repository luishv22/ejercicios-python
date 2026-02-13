#Programa que recibe un número
#y muestra si es par o impar usando una función

def par_impar(numero):

    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El numero {numero} es impar")

numero = int(input("Ingrese un número: "))
par_impar(numero)
