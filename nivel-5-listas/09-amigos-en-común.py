# Amigos en comun

"""
Dos personas tienen su lista de amigos. Arma una lista con los amigos que tienen en común,
como hace una red social.
"""

amigos_ana = ["Lucía", "Mateo", "Sofía", "Tomás", "Valentina", "Julián", "Camila", "Bruno", "Martina", "Nicolás"]

amigos_luis = ["Sofía", "Tomás", "Agustina", "Pedro", "Lucía", "Franco", "Martina", "Emilia", "Diego", "Bruno"]

amigos_en_comun = []

for i in range(len(amigos_ana)):
    if amigos_ana[i] in amigos_luis:
        amigos_en_comun.append(amigos_ana[i])



print(f"Los amigos en común son {amigos_en_comun}")