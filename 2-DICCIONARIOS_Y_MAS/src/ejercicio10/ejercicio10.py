"""
correos = [
"ana@gmail.com",
"carlos@hotmail.com",
"maria@gmail.com",
"juan@yahoo.com",
"pedro@gmail.com",
"laura@hotmail.com"
]
# Usa bucles y funciones para:
# 1. Contar cuántos correos hay por dominio (diccionario)
# Esperado: {'gmail.com': 3, 'hotmail.com': 2, 'yahoo.com': 1}
# 2. Crear set de dominios únicos
# 3. Encontrar el dominio más popular (recorre el diccionario del punto 1)
# 4. Lista de usuarios que usan gmail (usa bucle for con filtro if)
"""

correos = [
"ana@gmail.com",
"carlos@hotmail.com",
"maria@gmail.com",
"juan@yahoo.com",
"pedro@gmail.com",
"laura@hotmail.com"
]

dominio = {}
for correo in correos:
    lista= []
    lista = correo.split("@")
    if lista[1] in dominio:
        dominio[lista[1]] += 1
    else:
        dominio[lista[1]] = 1
        
print(dominio)

dominios_unicos = set(dominio)
print(dominios_unicos)

popular = [clave for clave, valor in dominio.items() if valor == max(valor for valor in dominio.values())]
print(popular)

lista_gmail=[]
for correo in correos:
    lista= []
    lista = correo.split("@")
    if lista[1] == "gmail.com":
        lista_gmail.append(lista[0])
            
print(lista_gmail)
    