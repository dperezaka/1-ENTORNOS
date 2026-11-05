"""
Dada una lista de números, crea una nueva lista que contenga solo los números mayores que 50.
numeros = [23, 67, 45, 89, 12, 55, 78, 34, 91]
"""

numeros = [23, 67, 45, 89, 12, 55, 78, 34, 91]
print(", ".join(str(n) for n in numeros))

altos = [i for i in numeros if i > 50]
print(", ".join(str(j) for j in altos))

