# if, if-else e if-elif-else

idade =int(input('qual a sua idade? '))

if idade >= 18:
    print('você é maior de idade, pode entrar')
else:
    print('Você é menor de idade, volte quando for maior de 18 anos')


nota1 = float(input('qual a primeira nota? '))
nota2 = float(input('qual a segunda nota? '))
nota3 = float(input('qual a terceira nota? '))
media = ((nota1 + nota2 + nota3) / 3)

if media >= 9:
    print(f'parabéns sua nota é {media} a perfeita')
elif media >= 8:
    print(f'Sua média é {media} boa nota!')
elif media >= 7:
    print(f'sua média é {media} bom.')
else:
    print(f'sua média é {media} tem que melhorar')
