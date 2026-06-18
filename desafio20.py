#criar um script que embaralha a ordem de apresentação de 4 alunos
import random

nome1=(input('Digite o nome da primeiro aluno: '))
nome2=(input('Digite o nome da segundo aluno: '))
nome3=(input('Digite o nome da terceiraoaluno: '))
nome4=(input('Digite o nome da quarto aluno: '))

lista=[nome1, nome2, nome3,nome4] # tranferir todas as alunas para uma lista.

random.shuffle(lista)

print(f'A ordem de apresentação do trabalho vai ser : \n {lista}')