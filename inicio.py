import os
import ecb as ecb


os.system('clear')
print('Ingrese el nombre de la imagen : ',end='')
nombre=input()

print('2: cifrar y 1: decifrar\nIngrese su opcion : ',end='')
op=int(input())

if op==2:
	ecb.encrypt_image(nombre, nombre[:nombre.index('.')]+'_eECB.bmp', 'key.bin')
elif op==1:
	ecb.decrypt_image(nombre, nombre[:nombre.index('.')]+'_dECB.bmp', 'key.bin')


