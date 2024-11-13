'''
Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola.
O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.
Organize o código em funções.
'''
alunos = {}
def menu():
    print( """
    ==================
    Menu Principal:
    1. Cadastrar Aluno
    2. Consultar Aluno
    3. Atualizar Aluno
    4. Excluir Aluno
    5. Sair
    ==================
    
    """)

def escolher_opcao():
    while True:
        menu()
        opcao = int(input("Digite sua opção:\n"))
        match(opcao):
            case 1:
                cadastrar_aluno()
            case 2:
                buscar_matricula = input("Digite a matrícula do aluno que deseja consultar: ")
                consultar_aluno(buscar_matricula)
            case 3:
                atualizar_aluno()
            case 4:
                excluir_aluno()
            case 5:
                break
            case _:
                print("Opção inválida!")
        
# Cadastrar aluno: Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
def cadastrar_aluno():
        aluno = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        curso = input("Digite o curso do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/yyyy): ")
        print(f"Aluno {aluno} cadastrado com sucesso!")
        alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
        return alunos
# Buscar um aluno por matrícula e exibir seus dados completos.
def consultar_aluno(buscar_matricula):
        if buscar_matricula in alunos:
            aluno_encontrado = alunos[buscar_matricula]
            print(f"Aluno encontrado: {aluno_encontrado['nome']}")
            print(f"Matrícula: {buscar_matricula}")
            return True
        else :
            print("Aluno não encontrado!")
            return False
# Atualizar dados do aluno:
'''def atualizar_aluno():'''#FAZER
    


def excluir_aluno():
    matricula = input("Qual a matrícula do aluno a ser excluído: ")
    achou = consultar_aluno(matricula)
    if achou:    
        del alunos[matricula]
        print("Aluno excluído com sucesso!")
    else: 
        print("Matrícula não encontrada.")    


escolher_opcao()

print(alunos.items())
