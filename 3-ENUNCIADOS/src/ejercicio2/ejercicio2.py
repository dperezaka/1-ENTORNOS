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

promedio =  {}

for clave, valor in calificaciones.items():
    print(clave)
    print(", ".join(str(n) for n in valor))
    suma = 0
    promedio[clave] =  sum(i for i in valor) / len(valor)
    
print(promedio)

for clave, valor in promedio.items():
    if max(promedio.values()) == valor:
        print(f"{clave} : {valor}")
        
numero_aprobados = 0

for valor in promedio.values():
    if valor >= 5:
        numero_aprobados +=1

print(numero_aprobados)

lista_aprobados={}
for clave, valor in promedio.items():
    if valor >= 5:
        lista_aprobados[clave] = valor
        
print(lista_aprobados)

    


    

    
    