import os
os.system("clear")

#mutabilidad
a = 5
b = a
print(id(a))

print("posicion 1:", id(a))
print("posicion 2:", id(b))

a = 9
print("posicion 3:", id(a))