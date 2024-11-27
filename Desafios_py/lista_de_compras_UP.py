'''
Esse desafio consiste em somar os itens de uma lista de compra.

- [x] Organizar os códigos em funções
- [x] Criar uma função para salvar a lista e o total em um arquivo txt.
- [x] Criar uma nova opção no menu para salvar a lista.

Nova fase criando a lista de produtos (CRUD):
- [ ] Criar uma lista de produtos e salvar em arquivo txt
- [ ] Carregar a lista de produtos de um arquivo txt;
- [ ] Atualizar a lista adicionando novos produtos;
- [ ] Deletar um produto da lista

'''

produtos = {'Arroz': 5.90, 
            'Macarrão': 3.60,
            'Feijão': 8.50,
            'Carne': 50.90,
            'Frango':20.00,}

#Carrinho
carrinho = []

# Mostrando produtos 
def mostrar_produtos():
    print('Produtos Disponíveis:')
    for produto, valor in produtos.items():
        print(f"{produto}: R$ {valor}") 

# Adicionando produtos
def adicionar_produto(total_compras):
    adicione = input("Digite o nome do produto: ")
    if adicione in produtos:
        carrinho.append(adicione) #adiciona o produto ao carrinho
        total_compras += produtos[adicione] #soma o valor dos produtos adicionados
        print(f'{adicione} adicionado ao carrinho. Total até o momento: R$ {total_compras}')
    else:
        print("Produto não encontrado. Tente novamente.")
    return total_compras

# Menu
def mostrar_menu():
    total_compras = 0.0
    menu = '''
----------------------------------------
1 - Mostrar Produtos
2 - Adicionar Produtos
3 - Mostar Carrinho
4 - Finalizar Compras
5 - Sair
----------------------------------------
Digite o número da opção desejada:\n
'''
    while True:
        opcao = input(menu)
        if opcao == '1':
            mostrar_produtos()
        elif opcao == '2':
            total_compras = adicionar_produto(total_compras)
        elif opcao == '3':
            print("Produtos no carrinho: ")
            for produto in carrinho:
                print(produto)
        elif opcao == '4':
            print("\nProdutos escolhidos:", ', '.join(carrinho))
            print(f"Total da compra: R$ {total_compras}")
            break

'''def salvar_lista():'''





    




