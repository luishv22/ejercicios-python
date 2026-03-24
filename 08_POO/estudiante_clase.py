# Definición de la clase Estudiante
class Estudiante:
    
    # Constructor: se ejecuta cuando creamos un nuevo estudiante
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre      # Nombre del estudiante
        self.edad = edad          # Edad del estudiante
        self.carrera = carrera    # Carrera que estudia

    # Método para mostrar la información del estudiante
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")
    
    # Método para aumentar la edad en 1 año
    def cumplir_años(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")
    
    # Método para cambiar la carrera del estudiante
    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
        print(f"{self.nombre} ahora estudia {self.carrera}")


# Crear un objeto de la clase Estudiante
berenice = Estudiante("Berenice", 18 , "Licenciatura en Gastronomía")

# Llamar a los métodos del objeto
berenice.presentarse()         # Muestra sus datos
berenice.cumplir_años()        # Aumenta su edad
berenice.cambiar_carrera("Licenciatura en Ciencia Forense")  # Cambia su carrera
