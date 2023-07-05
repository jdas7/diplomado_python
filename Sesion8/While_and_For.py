import os
os.system("clear")


"""
import time

while True:
    dato = str(input(" Ingrese un numero de conteo: "))
    
    if dato.lower() == "q" or dato.lower() == "Exit":
        break
    dato = int(dato)
    contador = 1
    while True:
        print(contador)
        contador += 1
        time.sleep(0.5)
        if contador > dato:
            break
"""

numero = int(input(" Ingrese el numero de la multiplication que desa hacer: "))

for mult in range(1,11):
    result = numero * mult
    print('{0:<2} X {1:^2} = {2:>2}'.format(numero, mult, result))