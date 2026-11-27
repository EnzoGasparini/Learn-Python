# Validador de email

"""
Armá una función que reciba un email y devuelva True si es válido: tiene exactamente una @, no
empieza con @ y tiene un punto en la parte que viene después de la @.
"""

def comprobacion_emails(email):
    if email.count("@") == 1 and not email.startswith("@" ) :
        posicion = email.find("@")
        if "." in email[posicion+1:] and ".." not in email[posicion+1:]:
         return True
        else:
            return False
    else:
        return False


es_valido = comprobacion_emails("Enzo.gasparini77@gmail.com")

if es_valido:
    print("Es valido")
else:
    print("Es invalido")