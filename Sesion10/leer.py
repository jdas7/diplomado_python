import os
os.system("clear")

nombre_archivo = "listado.csv"
valor = 0
contador = 0
with open(nombre_archivo, "r") as archivo:
    # vamos a omitir el encabezado
    next(archivo, None)
    for linea in archivo:
        # Remover el salto de linea
        linea = linea.rstrip()
        # Ahora convertimos la linea a un argumento
        lista = linea.split(",")
        nombre = lista[0]
        Area = str(lista[1])
        precio = float(lista[2])
        
        print(f"Equipo: '{nombre}', Area: '{Area}', precio: '{precio}'", sep="")

        valor = valor + precio
        contador += 1
    promedio_precio = valor / contador
    print(f"Promedio: '{promedio_precio}'")