"""
matematicas = {"Ana", "Carlos", "María", "Juan"}
fisica = {"María", "Juan", "Luis", "Carmen"}
quimica = {"Ana", "Juan", "Carmen"}
# Encuentra:
# 1. Estudiantes en las tres materias (usa & tres veces)
# 2. Estudiantes solo en Matemáticas (usa -)
# 3. Estudiantes en al menos dos materias
"""

matematicas = {"Ana", "Carlos", "María", "Juan"}
fisica = {"María", "Juan", "Luis", "Carmen"}
quimica = {"Ana", "Juan", "Carmen"}


print(f"Esta en los 3 es con & ")
nombres = matematicas & fisica & quimica
print(nombres)

print(f"Esta solo en matematicas con - ")
nombres =   matematicas - fisica - quimica
print(nombres)

print(f"Esta en almenos 2 materias")
nombres =  ( matematicas & fisica ) | (matematicas & quimica ) | (fisica & quimica)

print(nombres)