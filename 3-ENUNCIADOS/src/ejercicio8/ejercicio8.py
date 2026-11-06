"""
Convierte la tupla (1, 2, 3) en lista, añade el número 4, y vuelve a convertirla en tupla.
"""

tupla1 = (1, 2, 3)
print(tupla1)

lista = list(tupla1)
print(lista)

lista.append(4)
print(lista)

tupla2=tuple(lista)
print(tupla2)