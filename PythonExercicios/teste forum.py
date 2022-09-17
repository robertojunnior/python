print('Cálculo de preço médio de Ações')

nome = input('Código do ativo? ')
nome = bool(input('Lote Padrão? {}'.format(1)))
Compra1 = int(input('Quantidade'))
Preço1 = float(input('Preço R$'))
Compra2 = int(input('Quantidade'))
Preço2 = float(input('Preço R$'))
Compra3 = int(input('Quantidade'))
Preço3 = float(input('Preço R$'))

Compras = Compra1 + Compra2 + Compra3 + Compra4 + Compra5

PM = Preço/Quantidade

Ativo = Compra1, Compra2, Compra3, Compra4, Compra5
print('Compras','Preço{}'.format(Compras))
for media in range(1):
    print ('{} a sua media em {} foi {}'.format(Ativo,Compras,PM))