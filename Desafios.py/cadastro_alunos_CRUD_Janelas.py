'''Criando uma janela para cadastro de alunos contendo o CRUD'''


import tkinter as tk
from tkinter import ttk
import openpyxl 



def enviar_dados():
    nome = nome_entry.get()
    nasc = nasc_entry.get()
    curso = curso_entry.get()
    matr = matr_entry.get()


    
# Criando a Janela
root = tk.Tk()
root.title("Cadastro de Alunos")

# Criar um frame para conter os widgets do formulario
frame = ttk.LabelFrame(root, text="Cadastrando aluno")
frame.grid(row=0,column=0, pady=5, padx=5)

# Entrando com o nome completo
nome_label = ttk.Label(frame, text="Nome Completo")
nome_label.grid(row=0, column=0, padx=5, pady=5)
nome_entry = ttk.Entry(frame)
nome_entry.grid(row=1, column=0, padx=5, pady=5)

# Data de nascimento
nasc_label = ttk.Label(frame, text="Data de Nascimento")
nasc_label.grid(row=0, column=1, padx=5, pady=5)
nasc_entry = ttk.Entry(frame)
nasc_entry.grid(row=1, column=1, padx=5, pady=5)

# Curso que deseja
curso_label = ttk.Label(frame, text="Curso")
curso_label.grid(row=2, column=0, padx=5, pady=5)
curso_entry = ttk.Entry(frame)
curso_entry.grid(row=3, column=0, padx=5, pady=5)

# Matricula
matr_label = ttk.Label(frame, text="Matrícula")
matr_label.grid(row=2, column=1, padx=5, pady=5)
matr_entry = ttk.Entry(frame)
matr_entry.grid(row=3, column=1, padx=5, pady=5)

# Botão para inserir o aluno
button_inserir = ttk.Button(frame, text="Confirmar", command=enviar_dados)
button_inserir.grid(row=4, column=0, columnspan=2)














root.mainloop()
