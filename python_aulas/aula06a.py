
n1 = int(input('digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s) este Formato é antigo utilizado no Python 2
print('A soma entre {} e {} vale {}'.format(n1, n2, s)) #sintaxe nova, utilizando .format


