'''
Faça um algoritmo para ler três números e imprimir o maior.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))


if n1 > n2 > n3:
    print(f'O maior é: {n1}')

if n1 < n2 > n3:
    print(f'O maior é: {n2}')

if n1 < n2 < n3:
    print(f'O maior é: {n3}')

elif n1 == n2 == n3:
    print("Os números são iguais!")
