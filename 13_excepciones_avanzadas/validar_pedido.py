# Se crean las excepciones personalizadas heredando de Exception
class ErrorCantidad(Exception):
    pass
class ErrorPrecio(Exception):
    pass

# Lista de pedidos en productos
pedidos = [
    {"producto": "Laptop",  "cantidad": 2,  "precio": 15000},
    {"producto": "Mouse",   "cantidad": -1, "precio": 350},
    {"producto": "Teclado", "cantidad": 1,  "precio": -800},
    {"producto": "Monitor", "cantidad": 0,  "precio": 5000},
]

# Función que valida el pedido
def validar_pedido(pedido):
    # Verifica que el pedido no sea igual o menor a 0
    if pedido['cantidad'] <= 0:
        # Si el pedido es invalido, lanza la excepción ErrorCantidad
        raise ErrorCantidad(f"Cantidad inválida: {pedido['cantidad']}")
    
    # Verifica que el precio no sea igual o menor a 0
    if pedido['precio'] <= 0:
        # Si el precio es invalido, lanza la excepción ErrorPrecio
        raise ErrorPrecio(f"Precio invalido: {pedido['precio']}")
    
# Recorre cada pedido de la lista para validar 
for pedido in pedidos:
    try:
        # Intenta validar el pedido
        validar_pedido(pedido)
    # Captura la excepción si el pedido es igual o menor a 0 productos
    except ErrorCantidad as e:
        print(f"❎ Error con {pedido['producto']}: {e}")
    # Captura la excepción si el precio del producto es igual o menor a 0
    except ErrorPrecio as e:
        print(f"❎ Error con {pedido['producto']}: {e}")
    # Se ejecuta si no ocurrió ninguna excepción
    else:
        print(f"✅ {pedido['producto']} procesada correctamente")
    # Se ejecuta siempre, haya o ocurrido o no una excepción
    finally: 
        print("- revisado")
