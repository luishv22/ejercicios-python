class Estudiante:
    #Representa a un estudiante con nombre, edad y carrera
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    
class Salon:
    #Gestiona una lista de estudiantes dentro de un salón
    def __init__(self, nombre_salon):
        self.nombre_salon = nombre_salon
        self.estudiantes = []
          
    def agregar_estudiante(self, estudiante):
        #Agrega un objeto Estudiante a la lista del salón
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        #Imprime el nombre, edad y carrera de cada estudiante
        print(f"--- Salón: {self.nombre_salon} ---")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}, {estudiante.edad} años, {estudiante.carrera}")

    def total_estudiantes(self):
        #Retorna el número total de estudiantes en el salón
        return len(self.estudiantes)
    
    def promedio_edad(self):
        #Retorna el promedio de edad, o 0 si el salón esta vacío
        if not self.estudiantes:
            return 0
        return sum(estudiante.edad for estudiante in self.estudiantes) / len(self.estudiantes)
    
# Crear el salón
salon = Salon("Sistemas A")

# Crear estudiantes
axel     = Estudiante("Axel", 25, "Ingeniería Industrial")
berenice = Estudiante("Berenice", 19, "Gastronomía")
daniel   = Estudiante("Daniel", 23, "Ingeniería en Software")

# Agregar estudiantes al salón
salon.agregar_estudiante(axel)
salon.agregar_estudiante(berenice)
salon.agregar_estudiante(daniel)

# Mostrar reporte de salón
salon.mostrar_estudiantes()
print(f"Total: {salon.total_estudiantes()}")
print(f"Promedio de edad: {salon.promedio_edad():.2f}")
