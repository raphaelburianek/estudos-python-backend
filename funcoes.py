#funcoes

def saudacao():
    print('olá mundo!')

saudacao()
saudacao()

def saudacao1(nome):
    print(f'olá,{nome}')


saudacao1("joao")
saudacao1('maria')


def soma(a, b):
    return a + b
resultado = soma(4, 5)
print(resultado)


quadrado = lambda x: x ** 2
print(quadrado(5))

