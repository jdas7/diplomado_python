import os
os.system("clear")

# condicional anidado 

password =  input(" Ingrese su contraseña: ")

if (len(password) >= 8):
    print(" Contraseña válida")
    if (password == "miClaveSegura"):
        print(" Bienvenido")
    else:
        print(" Contraseña incorrecta")
else:
    print(" Contraseña es muy debil")
    
    if (password != "miClaveSegura"):
        print(" Contraseña incorrecta")