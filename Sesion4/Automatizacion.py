import os
os.system("clear")

sensor_a = 0 #si el sensor a, esta en 0 esta ok y si esta en 1, esta defectuoso. mide la altura
sensor_b = 0 #si el sensor b, esta en 0 esta ok y si esta en 1, esta defectuoso. mide el ancho
sensor_c = 0 #si el sensor c, esta en 0 esta ok y si esta en 1, esta defectuoso. mide la profundidad

if sensor_a == 0 and sensor_b == 0 and sensor_c == 0:
    print("Todos los sensores estan ok")
    print("La galleta esta perfecta: la galleta vale 10.000")
if sensor_a == 1 and sensor_b == 0 and sensor_c == 0:
    print("El sensor de altura detecto galleta con mucha arina: la galleta vale 9.000")
    print("La galleta esta defectuosa, pero puede pasar")
if sensor_a == 0 and sensor_b == 1 and sensor_c == 0:
    print("El sensor de ancho detecto galleta con mucha arina, la galleta vale 8.000")
    print("La galleta esta defectuosa, pero puede pasar")
if sensor_a == 0 and sensor_b == 0 and sensor_c == 1:
    print("El sensor de profunfundidad detecto galleta con mucha arina, la galleta vale 7.000")
    print("La galleta esta defectuosa, pero puede pasar")
if sensor_a == 1 and sensor_b == 1 and sensor_c == 0:
    print("El sensor de altura y ancho detecto galleta con mucha arina, la galleta vale 6.000")
    print("La galleta esta defectuosa, pero puede pasar")
if sensor_a == 1 and sensor_b == 0 and sensor_c == 1:
    print("El sensor de altura detecto galleta con mucha arina, la galleta vale 5.000")
    print("La galleta esta defectuosa, pero puede pasar")
if sensor_a == 1 and sensor_b == 1 and sensor_c == 1:
    print("la galleta no sirve para nada")
    print("La galleta esta defectuosa")
if sensor_a == 0 or sensor_b == 0:
    print("La galleta es excelente")