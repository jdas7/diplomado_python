import os
os.system("clear")

# programa para leer el archivo

dispisitivos = []
archivo = open("dispositivos.txt", "r")
for item in archivo:
    item = item.strip()
    dispisitivos.append(item)
archivo.close()
print(dispisitivos)