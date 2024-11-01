'''
Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar.
'''
while True:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print(f"Número {n} é par.")
    else: 
        print(f'Número {n} é impar.')
    continuar = input('Deseja continuar? (Digite s para sim)')
    if continuar != 's': break
