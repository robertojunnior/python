# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto: R$ '))
novopreço = preço - (preço * 5/100)

print('O preço de R$ {:.2f} do produto, com desconto de 5% é de R$ {:.2f}'.format(preço, novopreço))
