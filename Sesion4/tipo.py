import os
os.system("clear")

# Es python tipado dinamico
# Tipo de dato es entero o long
sensorT = 15
print(type(sensorT)) 

# Tipo de dato es float
sensorT = 1.
print(type(sensorT))

# Tipo de dato complejo
operacion = 1+1j
print(type(operacion), operacion)

# Tipo de dato String
sensorT = "HOLA"
print(type(sensorT))

# Tipo de dato booleano
sensorT = True
print(type(sensorT))

booleano = 5 == 4
print(type(booleano), booleano)

# Tipo de dato None
sensorT = None
print(type(sensorT))

# Tipo de dato lista
sensorT = []
print(type(sensorT))

# Tipo de dato tupla
sensorT = ("juan", "Perez", 25)
print(type(sensorT),sensorT)

# Tipo de dato diccionario
sensorT = {
    "a": 1,
    "b": 2
}
print(type(sensorT), sensorT)