'''
Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.
'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 % n2 == 0 :
    print('É divisível!')

else: 
    print('Não é divisível!')