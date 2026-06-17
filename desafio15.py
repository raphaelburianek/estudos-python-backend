#criar um script que calcule quantos dias a pessao ficou com o carro e a quilometragem rodada e mostre o valor total a pagar na tela.
# DIARIA R$ 60,00
#KM R$ 0,15 

diaria=int(input('quantos dias o cliente passou com o carro? '))
km=float(input('quantos km ele rodou com o carro? '))
diatotal=diaria*60.00
kmtotal=km*0.15
total=diatotal+kmtotal

print(f'o valor total que o clinte vai pagar é: R${total:.2f} Reais\nR${diatotal} Reais referente as diarias\nR${kmtotal:.2f} Reais referente a quilometragem rodada com o carro.')