#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input( 'Digite um número: '))
d = n * 2 #dobro
t = n * 3 #triplo
r = n ** (1/2)

print('O dobro de {} é igual à {}.'.format(n,d))
print('O triplo de {} é igual à {}. \nA raiz quadrada de {} é igual à {:.2f}.'.format(n,t,n,r))