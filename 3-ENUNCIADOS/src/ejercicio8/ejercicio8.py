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