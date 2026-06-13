#loops for e while e seus controles break continue e pass

frutas = ["maça", "banana", "mamao", "jaca"]

for fruta in frutas: #o loop for vai ler todos os itens de uma lista e mostrar na tela
    print(fruta)

for fruta in frutas:
    if fruta == "banana":
        break #vai parar o loop na hora que a fruta da lista for banana
    print(fruta)

contador = 0

while contador < 10: # o loop while vai contar enquanto nao chegar ao limite estabelecido
    print(contador)
    contador += 1



contador1 = 0   

while contador1 < 10:
    if contador1 == 5:
        break # para o codigo assim que o numero da contagem for 5
    print(contador1)
    contador1 += 1



for i in range(10):
    if i % 2 == 0: # nesse loop ele vai pular todos os numeros que seja divisivel por 2
        continue
    print(i)


for i in range(5):
    pass # passa faz o py ignorar esse bloco.