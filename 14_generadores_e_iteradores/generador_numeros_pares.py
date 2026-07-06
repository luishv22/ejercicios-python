# Genera números pares hasta el límite
def pares(limite):
  n = 0
  # Mientras no supere el límite
  while n <= limite:
    yield n  # Devuelve un número y pausa la función
    n += 2   # Suma 2 para obtener el siguiente par
   
# Recorre e imprime los números generados
for numero in pares(10):
  print(numero)
