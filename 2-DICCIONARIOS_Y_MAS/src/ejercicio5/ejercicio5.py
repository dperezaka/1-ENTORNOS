"""
# Dado tres diccionarios de ventas mensuales:
ventas_enero = {"A": 100, "B": 200}
ventas_febrero = {"A": 120, "B": 180, "C": 90}
ventas_marzo = {"A": 110, "C": 160}
# Crea un diccionario 'total' que sume las ventas de cada producto
# Si un producto no está en un mes, se cuenta como 0
# Usa bucles for para recorrer cada diccionario
# Esperado: {'A': 330, 'B': 380, 'C': 250}
"""

ventas_enero = {"A": 100, "B": 200}
ventas_febrero = {"A": 120, "B": 180, "C": 90}
ventas_marzo = {"A": 110, "C": 160}

total = dict()

def sumar_mes(ventas):
    try:
        for clave, valor in ventas.items():
            if clave in total:
                total[clave] += valor
            else:
                total[clave] = valor
    except ValueError:
        print("Falta un valor")
            
sumar_mes(ventas_enero)
sumar_mes(ventas_febrero)
sumar_mes(ventas_marzo)

print(total)