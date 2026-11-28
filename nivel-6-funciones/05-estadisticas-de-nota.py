# Estadísticas de notas

"""
Arma tres funciones que reciban una lista de notas: una devuelve el promedio, otra la mejor nota y
otra cuántos aprobaron (6 o más). Úsalas para mostrar el resumen de un curso.
"""

#notas = [8, 5, 7, 4, 10, 6, 3, 9, 7, 5, 8, 6]

def promedio(notas):
    sum_notas = 0
    for nota in notas:
        sum_notas += nota
    return sum_notas/len(notas)

def mejor_notas(notas):
    nota_mas_alta = 0
    for nota in notas:
        if nota_mas_alta < nota:
            nota_mas_alta = nota
    return nota_mas_alta

def aprobados(notas):
    alumnos_aprobados = 0
    for nota in notas:
        if nota >= 6:
            alumnos_aprobados += 1
    return alumnos_aprobados


lista_de_notas = [8, 5, 7, 4, 10, 6, 3, 9, 7, 5, 8, 6]

print("El promedio de notas es:", promedio(lista_de_notas))
print("La mejor nota es", mejor_notas(lista_de_notas))
print("La cantidad de alumnos aprobados es:" ,aprobados(lista_de_notas))