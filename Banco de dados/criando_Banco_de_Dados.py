'''
Atividade criar um CRUD:
Crie um banco de dados com o nome "banco_de_dados.db" e uma tabela chamada "clientes" com as seguintes colunas:
- id (chave primária, autoincremento)
- nome (varchar)
- email (varchar)
Algoritmo:
- [x] Criar o banco de dados
- [x] Criar a tabela de clientes
- [x] Inserir dados na tabela de clientes
- [x] Mostrar todos os clientes
- [x] Atualizar um cliente
- [x] Deletar um cliente
- [x] Fechar a conexão com o banco de dados
'''

import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent

#criar uma conexão com o banco de dados
conexao = sqlite3.connect(ROOT_PATH / 'data/banco_de_dados.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criando tabela de clientes
def criar_tabela_clientes():
    cursor.execute("""CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nome VARCHAR(100), 
               email VARCHAR(150))""")
    conexao.commit()

# Inserir dados na tabela
def inserir_clientes():
    cursor.execute(
    """INSERT INTO clientes (nome , email) VALUES 
    ('João', 'joao@gmail.com'),
    ('Maria', 'maria@gmail.com'),
    ('José', 'jose@gmail.com')
    """)
    conexao.commit()
    
# Atualizar Cadstros
def atualizar_registro():
    cursor.execute("UPDATE clientes SET nome = 'João da silva' where id = 1")
    conexao.commit()
    
# Excluir cadastro
def excluir_cadastro():
    cursor.execute(
        "DELETE FROM clientes WHERE id = 6"
    )
    conexao.commit()

# Ver Clientes
def mostrar_clientes():
  cursor.execute("SELECT * FROM clientes")
  for linha in cursor.fetchall():
    print(f"ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}")


"""Chamando funções"""
#criar_tabela_clientes()
#inserir_clientes()
#mostrar_clientes()
#atualizar_registro()
#excluir_cadastro()
'''------------------''' 

#Fechar conexão com banco de dados
conexao.close()
