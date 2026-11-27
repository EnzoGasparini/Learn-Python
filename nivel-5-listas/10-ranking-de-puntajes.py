# Ranking de puntajes

"""
Un juego guarda los puntajes de sus jugadores. Muestra los 3 mejores puntajes, de mayor a menor.

"""
puntajes = [85, 120, 95, 60, 150, 110, 75, 130, 100, 90]

primer_puesto = 0
segundo_puesto = 0
tercer_puesto = 0

for puntaje in puntajes:
    if puntaje > primer_puesto:
        tercer_puesto = segundo_puesto
        segundo_puesto = primer_puesto
        primer_puesto = puntaje
    elif puntaje > segundo_puesto:
        tercer_puesto = segundo_puesto
        segundo_puesto = puntaje
    elif puntaje > tercer_puesto:
        tercer_puesto = puntaje

print(primer_puesto)
print(segundo_puesto)
print(tercer_puesto)
