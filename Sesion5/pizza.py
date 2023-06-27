import os
os.system("clear")

print ("<<<<<<<<<<<<<<<<<<<<Pizzeria robotics>>>>>>>>>>>>>>>>>>>>>>>")
print ("El menu es el siguiente:")
print ("1. Pizza de champiñones", "17.000 pesos")
print ("2. Pizza de tomate", "16.000 pesos")
print ("3. Pizza hawaina", "18.000 pesos")
print ("4. Pizza de pollo", "19.000 pesos")
print ("***********************FIN**********************")

while True:
    print ("Ingrese la opcion que desea: ", "Marque si para comenzar")
    opcion = str(input("Ingrese Si para comenzar a transcribir su pedido: ")).lower()
    print ("Usted no digito: ", opcion)

    if opcion == "si":
        print ("¿ Que pizza quiere solicitar")
        pizza = int(input("Ingrese el numero de pizza que quiere: "))
        if pizza == 1:
            print ("Pizza de champiñone, estara lista en 5 min")
            print ("El precio de la pizza de Champiñones es de 17.000")
            metodo_pago = int(input("Desea pagar en efectifo o en TC: Marque 1 para efectivo y Marque 2 para tarjeta: "))
            if metodo_pago == 1:
                print ("Tu pago fue efectifo")
                ingreso_efectivo = int (input(" Por favor ingrese el efectivo: "))
                operacion = ingreso_efectivo - 17000
                print ("Usted ha ingresado: ", ingreso_efectivo, "Y su saldo es: ", operacion)
            if metodo_pago == 2:
                print ("Tu metodo de pago fue en tarjeta")
                print ("Acerque su tarjeta")
                ingreso_tarjeta = float (input(" Acerque su tarjeta para debitar:  "))
                operacion = ingreso_tarjeta - 17000
                print ("Usted ha ingresado: ", ingreso_tarjeta, "Y su saldo es: ", operacion)
            break
        if pizza == 2:
            print ("Pizza de tomate, estara lista en 5 min ")
            print ("El precio de la pizza de tomate es de 16.000")
            metodo_pago = int(input("Desea pagar en efectifo o en TC: Marque 1 para efectivo y Marque 2 para tarjeta: "))
            if metodo_pago == 1:
                print ("Tu pago fue efectifo")
                ingreso_efectivo = int (input(" Por favor ingrese el efectivo: "))
                operacion = ingreso_efectivo - 17000
                print ("Usted ha ingresado: ", ingreso_efectivo, "Y su saldo es: ", operacion)
            if metodo_pago == 2:
                print ("Tu metodo de pago fue en tarjeta")
                print ("Acerque su tarjeta")
                ingreso_tarjeta = float (input(" Acerque su tarjeta para debitar:  "))
                operacion = ingreso_tarjeta - 17000
                print ("Usted ha ingresado: ", ingreso_tarjeta, "Y su saldo es: ", operacion)
            break
        if pizza == 3:
            print ("Pizza hawaina, estara lista en 5 min ")
            print ("El precio de la pizza hawaina es de 18.000")
            metodo_pago = int(input("Desea pagar en efectifo o en TC: Marque 1 para efectivo y Marque 2 para tarjeta: "))
            if metodo_pago == 1:
                print ("Tu pago fue efectifo")
                ingreso_efectivo = int (input(" Por favor ingrese el efectivo: "))
                operacion = ingreso_efectivo - 18000
                print ("Usted ha ingresado: ", ingreso_efectivo, "Y su saldo es: ", operacion)
            if metodo_pago == 2:
                print ("Tu metodo de pago fue en tarjeta")
                print ("Acerque su tarjeta")
                ingreso_tarjeta = float (input(" Acerque su tarjeta para debitar:  "))
                operacion = ingreso_tarjeta - 18000
                print ("Usted ha ingresado: ", ingreso_tarjeta, "Y su saldo es: ", operacion)
            break
        if pizza == 4:
            print ("Pizza de pollo, estara lista en 5 min ")
            print ("El precio de la pizza de pollo es de 19.000")
            metodo_pago = int(input("Desea pagar en efectifo o en TC: Marque 1 para efectivo y Marque 2 para tarjeta: "))
            if metodo_pago == 1:
                print ("Tu pago fue efectifo")
                ingreso_efectivo = int (input(" Por favor ingrese el efectivo: "))
                operacion = ingreso_efectivo - 19000
                print ("Usted ha ingresado: ", ingreso_efectivo, "Y su saldo es: ", operacion)
            if metodo_pago == 2:
                print ("Tu metodo de pago fue en tarjeta")
                print ("Acerque su tarjeta")
                ingreso_tarjeta = float (input(" Acerque su tarjeta para debitar:  "))
                operacion = ingreso_tarjeta - 19000
                print ("Usted ha ingresado: ", ingreso_tarjeta, "Y su saldo es: ", operacion)
            break
        if pizza >= 5:
            print("No contamos con pizzas para la opcion ingresada")
    else:
        print ("Usted no digito una opción valida ")

print("muchas gracias por su compra")
        