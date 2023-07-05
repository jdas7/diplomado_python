import os
os.system("clear")
import time
# programa para revisar la conexión de energia

while True:
    conexion = int(input("Ingrese el estado de conexión: "))
    a = [1,2,3,4,5]
    if conexion == 0:
         for i in a:
            print(" Se desconectó la energia de la puerta ", i, "Puerta #2", end = " ")
            print("servo.values(1)")
            print("send email")
            time.sleep(1)
    else:
        print(" Esta conectado ")