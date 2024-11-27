'''
Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola. O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.
'''


alunos = {}

def main():
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            #Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
            aluno = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula: ")
            curso = input("Digite o nomne do curso: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
            alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
        elif opcao == "2":
            # Buscar um aluno por matrícula e exibir seus dados completos.
            buscar_matricula = input("Digite a matrícula do aluno que deseja consultar: ")
            if buscar_matricula in alunos:
                aluno_encontrado = alunos[buscar_matricula]
                print(f"Aluno encontrado: {aluno_encontrado['nome']}")
                print(f"Matrícula do aluno: {buscar_matricula}")
                print(f"Curso: {curso}")
                print(f"Data de nascimento: {data_nascimento}")
            else: print("Aluno não encontrado!")
        elif opcao == "3":
            # TODO excluir_aluno()
            pass
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

def cadastrar_aluno():
    # Implementar a funcionalidade de cadastro de aluno
    pass

def consultar_aluno():
    # Implementar a funcionalidade de consulta de aluno
    pass

def excluir_aluno():
    # Implementar a funcionalidade de exclusão de aluno
    pass

if __name__ == "__main__":
    main()