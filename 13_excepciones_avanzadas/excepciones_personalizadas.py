# Se crean dos excepciones personalizadas heredando de Exception
class ErrorEdad(Exception):
    pass

class ErrorSaldo(Exception):
    pass


# Lista de usuarios con sus datos
usuarios = [
    {"nombre": "Ana",   "edad": 25,  "saldo": 1500},
    {"nombre": "Luis",  "edad": -5,  "saldo": 800},
    {"nombre": "María", "edad": 200, "saldo": 300},
    {"nombre": "Pedro", "edad": 30,  "saldo": -100},
]

# Función que valida la información de un usuario
def validar_usuario(usuario):

    # Verifica que la edad esté dentro del rango permitido
    if usuario['edad'] < 0 or usuario['edad'] > 120:
        # Si la edad es inválida, lanza la excepción ErrorEdad
        raise ErrorEdad(f"Edad inválida: {usuario['edad']}")

    # Verifica que el saldo no sea negativo
    if usuario['saldo'] < 0:
        # Si el saldo es negativo, lanza la excepción ErrorSaldo
        raise ErrorSaldo(f"Saldo negativo: {usuario['saldo']}")


# Recorre cada usuario de la lista para validar sus datos
for usuario in usuarios:
    try:
        # Intenta validar al usuario
        validar_usuario(usuario)

    # Captura la excepción si existe un error en la edad
    except ErrorEdad as e:
        print(f"❎ Error con {usuario['nombre']}: {e}")

    # Captura la excepción si existe un saldo negativo
    except ErrorSaldo as e:
        print(f"❎ Error con {usuario['nombre']}: {e}")

    # Se ejecuta únicamente si no ocurrió ninguna excepción
    else:
        print(f"✅ {usuario['nombre']} registrada correctamente")

    # Se ejecuta siempre, haya ocurrido o no una excepción
    finally:
        print("- revisado")
