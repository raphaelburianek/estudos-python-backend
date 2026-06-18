#fazer um script que leia o cateto adj e o cateto oposto e ebtregue a ipotenusa ao usuario.

from math import hypot

co=float(input('digite o cateto oposto: '))
ca=float(input('digite o cateto adjacente: '))
hipotenusa= hypot(co, ca)

print(f'A hipotenusa  vai medir: {hipotenusa:.2f}') 

#lembra de desenvolver um script sem usar a biblioteca pra treinar mais a logica.