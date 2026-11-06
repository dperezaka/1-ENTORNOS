"""
Usa split() para dividir la cadena "Aprendo Python" en una lista de palabras. Luego, únelas con "-".
"""

cadena = "Aprendo Python"
print(cadena)

lista = []
lista = cadena.split(" ")
print(lista)

cadena2 = lista[0]+"-"+lista[1]
print(cadena2)