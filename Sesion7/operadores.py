import os
os.system("clear")

from math import sqrt


# calculadora ejemplo 
while True:
    a = int(input("Enter value a:"))
    b = int(input("Enter value b:"))

    print ("<<<<<<<<<<<<<<<<<<<<Bienvanidos a Unicalculadora>>>>>>>>>>>>>>>>>>>>>>>")
    print ("")
    print ("Estas son las opciones que puedo realizar:")
    print ("****************menú*******************")
    print ("")
    print ("1. suma")
    print ("2. resta")
    print ("3. multiplicación")
    print ("4. división")
    print ("5. modulo")
    print ("6. exponente")
    print ("7. raiz cuadrada")
    print ("8. división entera")
    print ("9. raiz cúbica")
    print ("")
    print ("***********************FIN**********************")

    print ("Calculadora dice: ¿Que operación desea hacer?: ")

    opcion = int(input("ingrese la operación que decea trabajar: "))
    print ("Calculadora dice: Usted escogio la opción ", opcion)
    print ("")

    if opcion == 1:
        print (a+b)
    elif opcion == 2:
        print (a-b)
    elif opcion == 3:
        print (a*b)
    elif opcion == 4:
        print (a/b)
    elif opcion == 5:
        print (a%b)
    elif opcion == 6:
        print (a**b)
    elif opcion == 7:
        print ("El resultado de la raiz de a: ", sqrt(a))
        print ("El resultado de la raiz de b: ", sqrt(b))
    elif opcion == 8:
        print (a//b)
    elif opcion == 9:
        print (a**3)
