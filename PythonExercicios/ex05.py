# Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e antecessor.

n = int(input('Digite um número: '))
#antecessor = n - 1
#sucessor = n + 1

#print('O antecessor é {}, e o Sucessor é o {}.'.format(antecessor, sucessor))

# Caso queira diminuir os comandos, basta apagar o Antecessor e sucessor linha 4 e 5, e colocalo
# da seguinte forma:

print('O antecessor é {}, e o Sucessor é o {}.'.format((n-1), (n+1)))