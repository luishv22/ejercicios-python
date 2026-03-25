# Definición de clase Rectángulo
class Rectangulo:
    # Constructor: se ejecuta al crear un rectángulo
    def __init__(self, base, altura):
        self.base = base       # Base del rectángulo
        self.altura = altura   # Altura del rectángulo

    # Calcula el área del rectángulo
    def area(self):
        return self.base * self.altura
    
    # Calcula el perímetro del rectángulo
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    # Muestra los datos del rectángulo
    def describir(self):
        print(f"Rectangulo de base {self.base} y altura {self.altura}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")

# Crear un Rectángulo de ejemplo
figura = Rectangulo(12, 6)
# Ejecutar el método principal
figura.describir()
