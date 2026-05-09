# Crear una lista con los estudiantes cuya calificación 
# sea diferente de 73
calf_diferente = [
    # Si la calificación es mayor o igual a 60
    # mostrar "APROBADO", si no "REPROBADO"
    f"{est['nombre']}: APROBADO" 
    if est['calificacion'] >= 60 
    else f"{est['nombre']}: REPROBADO" 

    # Recorrer cada estudiante de la lista
    for est in  estudiantes 

    # Filtrar estudiantes con calificación diferente de 73
    if est['calificacion'] != 73 
    ]

# Mostrar el resultado final
print(calf_diferente)
