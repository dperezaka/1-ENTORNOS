"""
def validar_contraseña(password):

Una contraseña válida debe:
- Tener al menos 8 caracteres
- Contener al menos una mayúscula
- Contener al menos una minúscula
- Contener al menos un dígito
Usa bucles for para las validaciones.
Devuelve (bool, str) con el resultado y mensaje


# Pruebas
print(validar_contraseña("Hola123")) # (True, "Válida")
print(validar_contraseña("hola123")) # (False, "Falta mayúscula")
print(validar_contraseña("HOLA123")) # (False, "Falta minúscula")
print(validar_contraseña("HolaHola")) # (False, "Falta dígito")
"""


def introduce_contraseña():
    print("""
          Una contraseña válida debe:
        - Tener al menos 8 caracteres
        - Contener al menos una mayúscula
        - Contener al menos una minúscula
        - Contener al menos un dígito
        """)
    password = input("Introduce una contraseña:\n>")
    return(password)
    
def validar_contraseña(password):
    prueba = True
    fallo = []
    if len(password) < 8:
        prueba = False
        fallo.append("1")
    mayuscula = False
    minuscula = False
    digito = False
    for n in password:
        if n in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            mayuscula = True
            fallo.append("2")
        if n in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            minuscula = True
            fallo.append("3")
        if n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            digito = True
            fallo.append("4")
    if not (mayuscula == True and minuscula == True and digito == True):
        prueba = False
    return (prueba, fallo)



prueba = False
while prueba == False:
    prueba = False
    password = introduce_contraseña()
    print("He introducido contraseña")
    prueba, fallo = validar_contraseña(password)
    print(f"prueba es {prueba}")
    print(f"fallo es {fallo}")
    if prueba == True:
        print("Es valido")
    if "1" in fallo:
        print("Numero")
    if "2" not in fallo:
        print("Falta mayúscula")
    if "3" not in fallo:
        print("Falta minúscula")
    if "4" not in fallo:
        print("Falta dígito")