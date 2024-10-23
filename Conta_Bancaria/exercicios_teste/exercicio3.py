'''
Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.

'''

while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    if n1 > n2:
        print(f'O valor {n1} é maior que {n2}')
    if n1 < n2: 
        print(f'O valor {n2} é maior que {n1}')
    else:
        print(f'Os valores são iguais')
    continuar = input('Deseja sair ? (Digite s para sair)')
    if continuar == 's': break
