"""
Crea una agenda que use diccionarios:
contactos = {}
def agregar_contacto(nombre, telefono, email):
contactos[nombre] = {"telefono": telefono, "email": email}
def buscar_contacto(nombre):
return contactos.get(nombre, "No encontrado")
def mostrar_todos():
# Implementar
pass
# Prueba tu código
agregar_contacto("Ana", "912345678", "ana@email.com")
buscar_contacto("Ana")
"""

contactos = {}

def agregar_contacto(nombre, telefono, email):
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(contactos[nombre])
    
def buscar_contacto(nombre):   
    return contactos.get(nombre, "No encontrado")

def mostrar_todos():
    print(contactos)
    

agregar_contacto("Ana", "912345678", "ana@email.com")
agregar_contacto("Pedro", "649568231", "pedro@email.com")
agregar_contacto("Juan", "juantel", "juan@email.com")
print("*"*60)
contacto = buscar_contacto("Ana")
print(contacto)
print("*"*60)
mostrar_todos()