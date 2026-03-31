# Definición de la clase Producto
class Producto:
    # Constructor que se ejecuta al crear el nuevo producto
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre               
        self.precio = precio                
        self.cantidad = cantidad            
    
    # Calcula el valor total del inventario de este producto
    def valor_total(self):
        return self.precio * self.cantidad
        
    # Aplica un descuento al precio del producto 
    def aplicar_descuento(self, porcentaje):
        descuento_decimal = porcentaje / 100
        self.precio = self.precio * (1 - descuento_decimal)
        print(f"{self.nombre} ahora cuesta: {self.precio:.2f}")

    # Muestra la información del producto
    def descripcion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio:.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Valor de inventario: {self.valor_total():.2f}")

# Lista de productos (objetos de la clase producto)
productos = [
    Producto("Laptop", 1000, 2),
    Producto("Mouse", 200, 3),
    Producto("Teclado", 500, 3)
]

total = 0

# Recorre cada producto y ejecuta su métodos principales
for producto in productos:
    producto.descripcion()
    producto.aplicar_descuento(15)
    total += producto.valor_total()
    print("-" * 30)
# Muestra el valor total del inventario después del descuento 
print(f"Inventario final: {total:.2f}")
