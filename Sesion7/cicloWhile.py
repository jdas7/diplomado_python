import os
os.system("clear")
import time

"""
while (True):
    print (" soy un ciclo repetitivo")
    time.sleep(1)
    """
    
"""    
i = 1
while (i<=4):
    print (i)
    i = i + 1
    print (i, end=' ')
    """

cont = 0
bandera = True 

while (bandera):
    print (cont)
    cont += 1
    time.sleep(1)
    if cont == 5:
        print ("El tanque esta medio lleno")
        continue
    if cont == 8:
        print ("El tanque esta casi lleno")
        continue
    if cont == 10:
        print ("El tanque esta lleno")
        bandera = False
