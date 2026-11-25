# Calificaciones

"""
Clasificación de una nota
Pedí una nota del 1 al 10 y el nombre del alumno, muestra el resultado y a que alumno corresponde:
- De 1 a 3: Insuficiente
- De 4 a 6: Aprobado
- De 7 a 8: Bueno
- De 9 a 10: Excelente
Si la nota está fuera de ese rango, muéstrale un mensaje de error.
"""

alumno = input("Ingrese el nombre del alumno: ")
nota = int(input("Ingrese la nota del alumno: "))
nora_final = ""

if nota >= 1 and nota <= 3:
    nota_final = "Insuficiente"
elif nota >= 4 and nota <= 6:
    nota_final = "Aprobado"
elif nota >= 7 and nota <= 8:
    nota_final = "Bueno"
elif nota >= 9 and nota <= 10:
    nota_final = "Excelente"
else:
    print("Error de carga")
    exit()

print(f"La nota final del alumno {alumno} es: {nota_final}")
