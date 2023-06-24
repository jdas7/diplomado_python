import os
os.system("clear")

print ("Wall-e dice: " "Hola como estas?, soy un router")
response_name = (input("Wall-e dice: ¿cual es tu nombre?: "))
print ("Hola",response_name, "Bienvenido, en este momento te puedo atender.")
print ("Wall-e dice: desea ver el estado de la conexion a red? o tengo vatias opciones")
print ("***********************MENÚ**********************")
print ("1. Estado de la conexion a red")
print ("2. Modelo de la conexion a red")
print ("3. Salir")
print ("***********************FIN**********************")

response = (input("Ingrese su opcion: "))

if response == "1":
    print ("Estado: Activo")
elif response == "2":
    print ("Modelo: s1654")
elif response == "3":
    print ("Adios")