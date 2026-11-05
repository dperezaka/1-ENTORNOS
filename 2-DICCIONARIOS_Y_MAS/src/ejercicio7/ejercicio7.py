"""
texto =
Python es un lenguaje de programación interpretado cuya filosofía
hace hincapié en la legibilidad de su código. Python es muy popular.
Python es poderoso y Python es fácil de aprender.

# 1. Cuenta frecuencia de cada palabra (diccionario)
# 2. Encuentra la palabra más frecuente
# 3. Muestra las palabras ordenadas alfabéticamente
"""

texto = "Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Python es muy popular. \
Python es poderoso y Python es fácil de aprender."

palabras = []

palabras = texto.split(" ")

print(palabras)

diccionario = dict()

for palabra in palabras:
    if palabra not in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1
        
print(diccionario)

maximo = max(diccionario.values())
palabra_maxima = []
for palabra, valor in diccionario.items():
    if valor == maximo:
        palabra_maxima.append(palabra)

print(palabra_maxima)

ordenado = dict(sorted(diccionario.items())) 
print(ordenado)