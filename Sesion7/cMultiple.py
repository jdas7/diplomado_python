import os
os.system("clear")

# pregunta al usuario por la renta
"""
renta = float(input(" cuantos fueron tus ingresos anuales? : "))

if renta < 1000:
    tipo = 5 # 5 % de impuestos
elif renta >= 1000 and renta < 5000:
    tipo = 4 # 4 % de impuestos
elif renta >= 5000 and renta < 10000:
    tipo = 3 # 3 % de impuestos
elif renta >= 10000 and renta < 20000:
    tipo = 2 # 2 % de impuestos
    
    """

# sensor de nivel

sensorN =  0

while True:
    
    if sensorN == 8:
        print (" El tanque esta full")
        time.sleep(2)
    elif sensorN == 5:
        print (" El tanque esta en nivel medio")
        time.sleep(2)
    elif sensorN == 2:
        print (" El tanque esta nivel bajo")
        time.sleep(2)
    elif sensorN == 0:
        print (" El tanque esta vacio")
        time.sleep(2)
    else:
        print (" El tanque esta lleno")
        time.sleep(2)