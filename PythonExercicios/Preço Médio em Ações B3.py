print('Tabela de cálculo para preço médio de Ações na B3')
#Caso queira calcular mais lotes, basta adicionar mais compras.

n1 = input('Digite o Códido do Ativo: ')

print('Obs: Caso os valores e quantidades sejam vazios, preencher "0".')

compra = float(input('Qual valor total da 1ª compra R$: '))
quant1 = int(input('Digite a Quantidade da 1ª compra: '))

segunda_compra = float(input('Qual valor total da 2ª compra R$ '))
quant2 = int(input('Digite a Quantidade da 2ª compra: '))

terceira_compra = float(input('Qual valor total da 3ª compra R$ '))
quant3 = int(input('Digite a Quantidade da 3ª compra: '))

Ativo = n1

Preco_Medio = (compra + segunda_compra + terceira_compra)/(quant1 + quant2 + quant3)

print('Seu preço médio em "{}" é de R$ {:.2f}'.format(n1, Preco_Medio),'por Ativo.')




