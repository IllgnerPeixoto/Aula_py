'''

Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos.

'''
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

soma = n1 + n2 + n3 
print(f'Soma dos valores é: {soma}')

media = soma / 3
print(f'Média dos valores é: {media}')

produto = n1 * n2 * n3
print(f'Produto dos valores é: {produto}')
