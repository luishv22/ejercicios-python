# Lista de tareas con su estado
tareas = [
{"titulo": "Estudiar Python", "estado": True},
{"titulo": "Hacer ejercicio", "estado": False},
{"titulo": "Leer un libro",   "estado": False},
{"titulo": "Cocinar",         "estado": True},
]

# Genera únicamente las tareas pendientes
def tareas_pendientes(tareas):
  # Recorre cada tarea
  for tarea in tareas:
    # Verifica si no está completada
    if not tarea["estado"]:
      yield tarea

# Muestra las tareas pendientes
for tarea in tareas_pendientes(tareas):
  print(f"❎ {tarea['titulo']}")
