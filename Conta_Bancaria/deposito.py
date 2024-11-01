saldo_inicial = 0
saldo = saldo_inicial

deposito = float(input('Digite o valor desejado para o despósito: '))
saldo += deposito
if deposito >= 0.1:
    print('Depósito realizado com sucesso!')
else: 
    print('Não foi possível realizar o depósito!')

print(f'Seu saldo é: {saldo}')
