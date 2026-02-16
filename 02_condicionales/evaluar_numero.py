# Programa que recibe un número 
# y evalúa si es positivo, negativo o cero

def evaluar_numero(numero):

    # Evaluación de número
    if numero > 0:
        return "Positivo"
    elif numero < 0: 
        return "Negativo"
    else:
        return "Cero"


num = int(input("Ingresa un número : "))
resultado = evaluar_numero(num)
print(f"El número es {resultado}")
