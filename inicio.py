import os
import ecb as ecb


os.system('clear')
print('Ingrese el nombre de la imagen : ',end='')
nombre=input()

print('1: cifrar y 2: decifrar\nIngrese su opcion : ',end='')
op=int(input())

ecb.inicio(nombre,op)

