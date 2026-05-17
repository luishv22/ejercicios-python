# Modifica la lista de inventario aplicando un descuento del 10% 

# Diccionario original con productos y precios
inventario = {
    "laptop":   15000,
    "mouse":    350,
    "teclado":  800,
    "monitor":  5000,
    "webcam":   1200,
}

# Crea un nuevo diccionario aplicando un descuento del 10%
descuento = {
    # Calcular el nuevo precio con descuento 
    producto: precio * (1 - 10/100)
    # Recorrer cada producto y precio del inventario
    for producto, precio in inventario.items()
}
# Mostrar el diccionario final con descuentos
print(descuento)
