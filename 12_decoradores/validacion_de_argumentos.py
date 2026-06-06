# Decorador que verifica que el argumento recibido sea mayor a 0.
# Si no lo es, muestra un mensaje de error sin ejecutar la función.
def validar_positivo(funcion):

    # Función envoltura que recibe el argumento de la función original
    def envoltura(n):

        # Verifica si el argumento es menor o igual a 0 
        if n <= 0:

            # Muestra un mensaje de error
            print("Error: el número debe ser positivo")
            return
        
        # Retorna el resultado de la función original
        return funcion(n)
    
    # Retorna la función modificada
    return envoltura

# Aplica el decorador a la función calcular_raiz
@validar_positivo
def calcular_raiz(n):

    # Retorna la raiz cuadrada del argumento
    return n ** 0.5

# Ejecuta la función decorada
print(calcular_raiz(9)) 
print(calcular_raiz(-4)) 
