# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.
# Considere o dólar 5,64.

print('Coversor de Reais em Dólar.')

valor = float(input("Digite valor em Reais: "))
d = valor * 5.64

print('O valor de {} convertido em dólar é de {:.2f}.'.format(valor,d))
