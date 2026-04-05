class Persona:
    # Representa a una persona con nombre y edad
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        # Muestra un saludo con la información de la persona
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    # Representa a un estudiante, heredando de Persona
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        # Muestra la carrera que está estudiando
        print(f"{self.nombre} está estudiando {self.carrera}")

class Profesor(Persona):
    # Representa a un profesor, heredando de Persona
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        # Muestra la materia que imparte el profesor
        print(f"El profesor {self.nombre}, enseña {self.materia}")

# Crea instancias de estudiante y profesor
luis = Estudiante("Luis", 23, "Ingeniería en Sistemas")
eduardo = Profesor("Eduardo", 45, "Calculo integral")

# Mostrar saludo e información del estudiante
luis.presentarse()
luis.estudiar()

# Mostrar saludo e información del profesor
eduardo.presentarse()
eduardo.enseñar()
