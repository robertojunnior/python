# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Cálculo de média entre duas notas de um aluno!')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

media = (n1 + n2)/ 2
print('A média entre {} e {} é igual à {:.1f}.'.format(n1,n2,media))

