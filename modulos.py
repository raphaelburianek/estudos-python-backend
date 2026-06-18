from math import sqrt, floor
num=int(input('digite um numero: '))
raiz=sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz):.2f}.')



import random

num=random.random() #escolhe um numero aleatorio, podendo ser float
num2=random.randint(1,10)  #escolhe um numero inteiro, e os paremtros entre 1 e 10
print(num)
print(num2)


import emoji

print(emoji.emojize('Olá mundo :sunglasses:', language='alias'))
