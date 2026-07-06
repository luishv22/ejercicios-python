# Lista de tareas con su estado
tareas = [
{"titulo": "Estudiar Python", "estado": True},
{"titulo": "Hacer ejercicio", "estado": False},
{"titulo": "Leer un libro",   "estado": False},
{"titulo": "Cocinar",         "estado": True},
]

# Generador que obtiene las tareas completadas
tareas_completadas = (
    f"✅ {tarea['titulo'].upper()}"
    for tarea in tareas
    if tarea["estado"]  # Solo incluye tareas completadas
)

# Recorre e imprime las tareas completadas
for tarea in tareas_completadas:
  print(tarea)
