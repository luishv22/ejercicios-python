# Programa que pide al usuario su contraseña
# y verifica que sea correcta

def contraseña_correcta():
    contraseña = ""

    while contraseña != "python123":

    # pide contraseña al usuario
        contraseña = input("Ingrese la contraseña: ")

    # verifica contraseña correcta
        if contraseña != "python123":
            print("Contraseña incorrecta.")

    print("Acceso concedido")

contraseña_correcta()
