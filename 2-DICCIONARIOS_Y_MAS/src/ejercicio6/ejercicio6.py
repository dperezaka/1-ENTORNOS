"""
# Dado un diccionario de estudiantes y sus ciudades
estudiantes = {
"est001": {"nombre": "Ana", "ciudad": "Madrid"},
"est002": {"nombre": "Carlos", "ciudad": "Barcelona"},
"est003": {"nombre": "María", "ciudad": "Madrid"}
}
# Crea un diccionario agrupado por ciudad
# Esperado: {'Madrid': ['Ana', 'María'], 'Barcelona': ['Carlos']}
"""


estudiantes = {
"est001": {"nombre": "Ana", "ciudad": "Madrid"},
"est002": {"nombre": "Carlos", "ciudad": "Barcelona"},
"est003": {"nombre": "María", "ciudad": "Madrid"}
}

agrupado = {}

for est in estudiantes.keys():
    if estudiantes[est]["ciudad"] in agrupado:
        agrupado[estudiantes[est]["ciudad"]].append(estudiantes[est]["nombre"])
    else:
        agrupado[estudiantes[est]["ciudad"]] = [estudiantes[est]["nombre"]]
            
print(agrupado)