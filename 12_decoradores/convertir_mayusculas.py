# Decorador que convierte a mayúsculas
# el resultado retornado por una función 
def mayusculas(funcion):

    # Función decoradora que recibe cualquier cantidad 
    # de argumentos posicionales y nombrados
    def envoltura(*args, **kwargs):

        # Ejecuta la función original
        resultado = funcion(*args, **kwargs)

        # Convierte el resultado a mayúsculas 
        return resultado.upper()
    
    # Retorna la función modificada
    return envoltura

# Aplica el decorador a la función saludo
@mayusculas
def saludo():

    # Retorna un mensaje en minúsculas 
    return "hola, mundo"

# Ejecuta la función decorada
print(saludo())
