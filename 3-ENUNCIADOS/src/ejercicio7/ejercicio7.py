"""
Crea un diccionario con {"manzana": 2, "banana": 5}:
1. Añade "naranja" con valor 3.
2. Imprime solo las frutas con cantidad mayor a 3.
"""

frutas = {"manzana": 2, "banana": 5}
print(frutas)

frutas["naranja"] = 3
print(frutas)

print([clave for clave, valor in frutas.items() if valor > 3])