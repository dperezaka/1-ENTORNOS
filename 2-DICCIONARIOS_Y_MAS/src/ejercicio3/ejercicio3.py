"""
def contar_palabras(texto):
Cuenta cuántas veces aparece cada palabra.
Devuelve un diccionario {palabra: cantidad}
texto = "python es genial python es poderoso python es facil"
resultado = contar_palabras(texto)
# Esperado: {'python': 3, 'es': 3, 'genial': 1, 'poderoso': 1, 'facil': 1}
"""


def contar_palabras(texto):
    palabras = []
    palabras = texto.split()
    contador = {}
    for n in palabras:
        if n in contador:
            contador[n] +=1
        else:
            contador[n] =1
    return contador

entrada = str(input("Dame el texto a contar apariciones:\n>"))

respuesta = contar_palabras(entrada)

print(respuesta)