# Votacion

"""
En una votación hay tres candidatos: "Ana", "Luis" y "Sofía". Tienes la lista de votos, uno por
persona. Cuenta los votos de cada candidato y muestra el ganador. Si hay empate, avisa.
"""

votos = ["Ana", "Luis", "Sofía", "Ana", "Luis", "Ana", "Sofía", "Luis", "Ana", "Sofía", "Luis", "Ana"]
ana = 0
sofia = 0
luis = 0

for candidato in votos:
    if candidato == "Ana":
        ana += 1
    elif candidato == "Luis":
        luis += 1
    else:
        sofia += 1

print(f"{luis} votos para Luis")
print(f"{ana} votos para Ana")
print(f"{sofia} votos para Sofia")

if ana > luis and ana > sofia:
    print("Ana es la ganadora")
elif luis > ana and luis > sofia:
    print("Luis es el ganador")
elif sofia > ana and sofia > luis:
    print("Sofia es la ganadora")
else:
    print("Empate")
