"""
calificaciones = {
"Ana": [8.5, 9.0, 7.5, 8.0],
"Carlos": [6.0, 7.0, 6.5, 7.5],
"María": [9.5, 9.0, 9.2, 9.8]
}
# Calcula:
# 1. Promedio de cada estudiante (usa sum() y len())
# 2. Estudiante con mejor promedio (usa max())
# 3. Cuántos aprobaron (promedio >= 5)
# 4. Diccionario con solo aprobados (usa bucle for)
"""

calificaciones = {
"Ana": [8.5, 9.0, 7.5, 8.0],
"Carlos": [6.0, 7.0, 6.5, 7.5],
"María": [9.5, 9.0, 9.2, 9.8]
}

promedio = {}

for clave, valor in calificaciones.items():
    print(clave)
    print(valor)
    promedio[clave] = sum(n for n in valor)/ len(valor)

print(promedio)

maximo = [clave for clave,valor in promedio.items() if valor == max(n for n in promedio.values())]
print(maximo)

aprobados = [clave for clave, valor in promedio.items() if valor >=5]
print(", ".join(aprobados))

diccionario_aprobados={}
for clave, valor in promedio.items():
    if valor >=5:
        diccionario_aprobados[clave] = valor

print(diccionario_aprobados)