"""
1. Pide al usuario/a 3 números y guárdalos en una lista.
2. Convierte la lista a tupla.
3. Calcula la suma de los números y muestra el resultado.
"""

lista_numeros=[]
for n in range(3):
    numero = input("Dame un numero:\n>") # FALLARA CON CUALQUIER COSA QUE NO SEA ENTEROS
    lista_numeros.append(numero)
print(lista_numeros)

tupla_numeros = tuple(lista_numeros)
print(tupla_numeros)

print(sum(int(n) for n in tupla_numeros))