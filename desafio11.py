#converter a altura e largura de uma parede em metros quadrados.
altura=float(input('qual a altura da parede: '))
largura=float(input('qual a largura da parde: '))
area= altura*largura
tinta= area/2

print(f'a área total da sua parede é {area:.2f}m2, \nVamos precisar de {tinta:.2f} litros de tinta para pintar a parede toda.')