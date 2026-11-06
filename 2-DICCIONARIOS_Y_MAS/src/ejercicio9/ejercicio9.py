"""
inventario = {
"PRO001": {"nombre": "Laptop", "precio": 800, "stock": 15},
"PRO002": {"nombre": "Mouse", "precio": 20, "stock": 50},
"PRO003": {"nombre": "Teclado", "precio": 45, "stock": 5}
}
# Implementa:
# 1. valor_total_inventario() - suma precio * stock de todos
# 2. productos_bajo_stock(minimo) - lista productos con stock < minimo
# 3. producto_mas_caro() - devuelve tupla (codigo, nombre, precio)
# 4. aplicar_descuento(porcentaje) - reduce todos los precios
"""

inventario = {
"PRO001": {"nombre": "Laptop", "precio": 800, "stock": 15},
"PRO002": {"nombre": "Mouse", "precio": 20, "stock": 50},
"PRO003": {"nombre": "Teclado", "precio": 45, "stock": 5}
}

def valor_total_inventario():
    suma = 0
    for n in inventario:
        suma += inventario[n]["precio"]*inventario[n]["stock"]
    return suma

def productos_bajo_stock(minimo):
    falta = []
    for n in inventario:
        if inventario[n]["stock"] < minimo:
            falta.append(n)  
    return falta

def producto_mas_caro():
    carisimo = [clave for clave in inventario.keys() if inventario[clave]["precio"] == max(inventario[clav]["precio"] for clav in inventario.keys())]
    return carisimo


def aplicar_descuento(porcentaje):
    a_multiplicar= porcentaje / 100
    for clave , valor in inventario.items():
        inventario[clave]["precio"] = inventario[clave]["precio"] * (1 - a_multiplicar)
    

total = valor_total_inventario()
print(f"El total es de {total}")

minimos= productos_bajo_stock(16)
print(minimos)

caro = producto_mas_caro()
print(caro)

aplicar_descuento(10)
print(inventario)