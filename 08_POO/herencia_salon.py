class Persona:
    """Representa a una persona con nombre y edad."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """Muestra un saludo con la información de la persona."""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    """Representa a un estudiante, heredando de Persona."""
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        """Muestra la carrera que está estudiando."""
        print(f"{self.nombre} está estudiando {self.carrera}")

class Salon:
    """Gestiona una lista de estudiantes dentro de un salón."""
    def __init__(self, nombre_salon):
        self.nombre_salon = nombre_salon
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """Agrega un objeto Estudiante a la lista del salón."""
        if isinstance(estudiante, Estudiante):
            self.estudiantes.append(estudiante)
        else: 
            print("Error: solo se pueden agregar objetos de tipo Estudiante")

    def mostrar_estudiantes(self):
        """Imprime el nombre, edad y carrera de cada estudiante."""
        print(f"--- Salón: {self.nombre_salon} ---")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}, {estudiante.edad} años, {estudiante.carrera}")

    def total_estudiantes(self):   
        """Retorna el número total de estudiantes en el salón."""
        return len(self.estudiantes)
    
    def promedio_edad(self):
        """Retorna el promedio de edad, o 0 si el salón está vacío."""
        if not self.estudiantes:
            return 0
        return sum(estudiante.edad for estudiante in self.estudiantes) / len(self.estudiantes)

# Crea el salón
salon = Salon("Este A")

# Crea estudiantes
luis = Estudiante("Luis", 23, "Ingeniería en Sistemas")
axel = Estudiante("Axel", 22, "Ingeniería Industrial")
carlos = Estudiante("Carlos", 22, "Ingeniería en Software")

# Mostrar saludo e información del estudiante
for estudiante in [luis, axel, carlos]:
    estudiante.presentarse()
    estudiante.estudiar()

# Agregar estudiantes al salón
salon.agregar_estudiante(luis)
salon.agregar_estudiante(axel)
salon.agregar_estudiante(carlos)

# Mostrar reporte de salón
salon.mostrar_estudiantes()
print(f"Total: {salon.total_estudiantes()}")
print(f"Promedio de edad: {salon.promedio_edad():.2f}")
