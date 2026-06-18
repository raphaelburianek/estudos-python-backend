#criar um script que sorteia 1 em 4 nomes que o usuraio digitar
import random

nome1=(input('Digite o nome da primeira aluna: '))
nome2=(input('Digite o nome da segunda aluna: '))
nome3=(input('Digite o nome da terceira aluna: '))
nome4=(input('Digite o nome da quarta aluna: '))

lista=[nome1, nome2, nome3,nome4] # tranferir todas as alunas para uma lista.

sorteio=random.choice(lista) #a função choice escolhe direto da lista.

print(f'A aluna escolhida é: {sorteio}')