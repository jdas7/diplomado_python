import os
os.system("clear")

# Programa para desarrollar un condicional simple 
"""
clase_A = "10.0.0.50"
clase_B = "173.150.0.50"
clase_C = "192.168.10.2"

num_IPV4 = str(input("Ingrese una dirección IPV4: "))
print (num_IPV4)

if num_IPV4 == clase_A:
    print ("La dirección IPV4 es de la clase A", num_IPV4)
elif num_IPV4 == clase_B:
    print ("La dirección IPV4 es de la clase B", num_IPV4)
elif num_IPV4 == clase_C:
    print ("La dirección IPV4 es de la clase C", num_IPV4)
    
# -----------------------------------------------------------#

uno = 819
primerR = "Cisco 819 Roter"
dos = 881
segundoR = "Cisco 881 Roter"
tres = 888
terceroR = "Cisco 888 Roter"

nombreR = int (input("ingrese el numero de router: "))

if nombreR == uno or dos or tres:
    print ("Usted tiene un router", nombreR, "Cisco")
    """
# -----------------------------------------------------------#

print ("Ingrese su sueldo mensual: ")
sueldo = input()
ingresos = float (sueldo)
print ("Ingrese su egreso: ")
egreso = input()
egresos = float (egreso)
efectivo = ingresos - egresos

if efectivo > 0:
    print ("Efectivo: ", efectivo)