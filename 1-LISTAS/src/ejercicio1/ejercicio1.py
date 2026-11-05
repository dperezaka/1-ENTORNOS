"""
Crea una lista con los números del 1 al 10, luego:
Agrega el número 11 al final
Elimina el número 5
Ordena la lista en orden descendente
Muestra la longitud de la lista
"""

lista = [ n for n in range(1,11) ]
print(", ".join(str(x) for x in lista))

lista.append(11)
print("Agrego 11")
print(", ".join(str(x) for x in lista))

lista.remove(5)
print("Borro 5")
print(", ".join(str(x) for x in lista))

lista.sort(reverse = True)
print("Invierto")
print(", ".join(str(x) for x in lista))

print("Longuitud")
print(len(lista))


