# Aprobados y Desaprobados

"""
Dada una lista de notas, arma dos listas: una con las notas aprobadas (6 o más) y otra con las
desaprobadas. Muestra las dos y cuántas hay en cada una.
"""

notas = [8, 4, 6, 3, 10, 5, 7, 2, 6, 9, 1, 5,11 ]
aprobados = []
desaprobados = []

for nota in notas:
    if nota < 1 or nota > 10:
        print(f"La nota {nota} es inválida")
    elif nota >= 6:
        aprobados.append(nota)
    else:
        desaprobados.append(nota)

print(f"Notas de los alumnos aprobados {aprobados}, son {len(aprobados)} en total.")
print(f"Notas de los alumnos desaprobados {desaprobados}, son {len(desaprobados)} en total.")
