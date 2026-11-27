# Correos sin repetidos

"""
Una lista de correos para un newsletter tiene direcciones repetidas. Armá una lista nueva sin
repetidos, respetando el orden en que aparecen.
"""
lista_de_correos = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com", "b@mail.com"]
lista_sin_repetidos = []
for i in range(len(lista_de_correos)):
    if lista_de_correos[i] not in lista_sin_repetidos:
        lista_sin_repetidos.append(lista_de_correos[i])
print(f"La nueva lista de correos: {lista_sin_repetidos}")