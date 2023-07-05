import os
os.system("clear")

"""
# placeholder 
numero = int(input("Ingrese el número 1: "))
numero2 = int(input("Ingrese el número 2: "))
resultado = numero * numero2

# imprimir en formato String
print(numero,"X", numero2, "=", resultado)
print(f"{numero} X {numero2} = {resultado}")
print("El resultado es: " + str(resultado))
print('{} X {} = {}'.format(numero, numero2, resultado))
print('{0:<1} X {1:^1} = {2:>1}'.format(numero, numero2, resultado))
print("la multiplicación de, %s x %s = %s "%(numero, numero2, resultado))
print(F"El resultado es: {resultado}. ")
"""
"""
equipo = "Router"
cantidad = 10 

print(f"Hay {cantidad} equipos de tipo {equipo}")
"""
"""
import math

print(f"El valor de pi es: {math.pi}")
print(f"El valor de pi es: {math.pi:.2f}")
"""

a = 2
b = 128

c = a ** b
print(f'El valor final es: {c:2e} quintillones de direcciones IPV6 \"Son muchas\"')

print(f"{a:10} exp a la -------> {b:10}")

import datetime

fecha = datetime.datetime.now()
print(f'{fecha: %d - %m - %Y}')
