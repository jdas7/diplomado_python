import os
os.system("clear")
import time
import csv

nombre_archivo = "listado.csv"
valor = 0
contador = 0
with open(nombre_archivo, "r") as archive:
    lector = csv.reader(archive, delimiter=",")
    next(lector, None)
    for fila in lector:
        nombre = fila[0]
        area = fila[1]
        precio = float(fila[2])
        valor += precio
        contador += 1
    promedio = valor / contador
    print(f"Precio Total: {valor} contador: {contador}")
    print(promedio)