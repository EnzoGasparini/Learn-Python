# Contraseña fuerte

"""
Armá una función que verifique si una contraseña es fuerte: al menos 8 caracteres, un número y
una mayúscula. Devuelve True o False.
"""


def verificacion_pass(password):
    tiene_numeros = False
    tiene_mayusucula = False
    if len(password) >= 8:
        for catacter in password:
            if catacter.isdigit():
                tiene_numeros = True
            if catacter.isupper():
                tiene_mayusucula = True
    if len(password) >= 8 and tiene_numeros == True and tiene_mayusucula == True:
                return True
    else:
        return False


print(verificacion_pass("Enzuka123"))
