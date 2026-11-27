# Notas del curso

"""
Tenés las notas de un curso: [7, 4, 9, 6, 10, 3, 8]. Muestra el promedio, cuántos alumnos aprobaron
(6 o más) y la mejor nota.
"""

notas = [7, 4, 9, 6, 10, 3, 8]
alumnos_aprobados = 0
alumno_desaprobados = 0
nota_mas_alta = 0
total_notas = 0

for i in range(len(notas)):
    total_notas += notas[i]
    if nota_mas_alta < notas[i]:
        nota_mas_alta = notas[i]
    if notas[i] >= 6:
        alumnos_aprobados += 1
    else:
        alumno_desaprobados += 1

print(f"La cantidad de alumnos aprobados es de: {alumnos_aprobados} alumnos")
print(f"La cantidad de alumnos desaprobados es de: {alumno_desaprobados} alumnos")
print(f"El promedio de todas las notas es de: {total_notas / len(notas):.2f}")
print(f"La nota más alta del curso es: {nota_mas_alta}")
