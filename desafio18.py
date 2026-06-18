#criar um script que o usuario digite um raio e  receba o seno cosseno e tangente.
from math import sin, cos, tan, radians

angulo=float(input('Digite o ângulo que voçê deseja: '))

#transformar o angulo em radiano
raio=radians(angulo)

seno= sin(raio)
cosseno=cos(raio)
tangente=tan(raio)

print(f'O ângulo {angulo}° tem o seno  de {seno:.2f}'
      f'\ncosseno de {cosseno:.2f}'
      f'\nE o tangente de {tangente:.2f}')