"""
Crea un diccionario que cuente las letras de la palabra "programación". Usa get() para simplificar el código.
"""

palabra = "programación"

diccionario = {}
diccionario1 = {}
## SIN GET
for letra in palabra:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1


## CON GET
for letra in palabra:
    diccionario1[letra] = diccionario1.get(letra, 0) + 1
    
print(diccionario)
print(diccionario1)