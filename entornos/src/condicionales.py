import os
os.system("clear")


""" edad = int(input("Ingrese su edad: "))
if edad <= 18:
    print("Eres menor de edad", "Tienes: ", edad)
else:
    print("Eres mayor de edad", "Tienes: ", edad)

# programa para verificar contraseña

key = "contraseña"
password = input("Ingrese su contraseña: ")

if key == password.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
    
# programa para cañcular los numeros de la division
num = float(input("Ingrese un numero: "))
div = float(input("Ingrese un divisor: "))

if div <= 0:
    print("El divisor no puede ser cero o negativo")
else:
    print("El resultado de la division es: ", num/div)
    
# programa para mostrar si es par o impar

num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# programa para tributar 

edad = int(input("¿ cual es tu edad: "))
ingreso = float(input("Cuales son los ingresos mensuales: "))

if edad > 17 and ingreso >= 1000000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar") """
    
# programa para verificar el genero

nombre = input("¿como te llamas?: ")
genero = str(input("Ingrese su sexo (M o H): ")).lower()
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
    print("Es una mujer")
else:
    if nombre.lower() < "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es" + grupo)