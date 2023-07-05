import os
os.system("clear")

# programa para desarrolla una lista de dispositivos de red

archivo = open("dispositivos.txt", "a")

while True:
    nuevoEquipo = input("Ingrese el nombre del dispositivo: ")
    if nuevoEquipo == "salir":
        print("Bien hecho terminaste")
        break
    archivo.write(nuevoEquipo + "\n")
archivo.close()