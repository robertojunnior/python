# Cálculo de quantos litros de tinta por m².

# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-lo,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {:.2f} x {:.2f}, e sua área é de {:.2f}m²'.format(larg,alt,área))
tinta = área / 2
print('Para pintar esta parede, você vai precisar de {} litros de tinta.'.format((tinta)))
galao = 3.6
total = tinta/galao
print('E vai precisar comprar {:.2f}gl de tinta.'.format(total))

