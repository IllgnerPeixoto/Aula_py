import tkinter as tk
from tkinter import ttk

def enviar_dados():
  nome = nome_entry.get()
  idade = idade_spinbox.get()
  print(f"Nome: {nome}, Idade: {idade}")

#janela principal
window = tk.Tk()
window.title("Formulário de Entrada")

# Criar um frame para conter os widgets do formulario
frame = ttk.LabelFrame(window, text="Informações do Usuário")
frame.grid(row=0,column=0, pady=5, padx=5)

# nome
nome_label = ttk.Label(frame, text="Nome")
nome_label.grid(row=0, column=0, padx=5, pady=5)

#sobrenome
sobrenome_label = ttk.Label(frame, text="Sobrenome")
sobrenome_label.grid(row=0, column=1, padx=5, pady=5)

#Entrar com nome
nome_entry = ttk.Entry(frame)
nome_entry.grid(row=1, column=0, padx=5, pady=5)

#entrar com sobrenome
sobrenome_entry = ttk.Entry(frame)
sobrenome_entry.grid(row=1, column=1, padx=5, pady=5)

#idade
idade_label = ttk.Label(frame, text="Idade")
idade_label.grid(row=2, column=0, padx=5, pady=5)

#entrar com idade
idade_spinbox = ttk.Spinbox(frame, from_=18, to=100)
idade_spinbox.grid(row=3, column=0, padx=5, pady=5)

#Nacionalidade 
nacionalidade_label = ttk.Label(frame, text= "Nacionalidade")
nacionalidade_label.grid(row=2, column=1, padx=5, pady=5)

#Selecionar nacionalidade
nacionalidade_combobox = ttk.Combobox(frame, values=["Brasileiro", "Argentino", "Uruguaio", "Colombiano","Chileno"])
nacionalidade_combobox.grid(row=3, column=1,padx=5, pady=5)

# Tratamento
tratamento_label = ttk.Label(frame, text= "Tratamento")
tratamento_label.grid(row=0, column=2, padx=5, pady=5)

#Entrar com tratamento
tratamento_combobox = ttk.Combobox(frame, values=["Sr", "Sra", "Dr", "Dra","Nenhum"])
tratamento_combobox.grid(row=1, column=2, padx=5, pady=5)

'''enviar_button = ttk.Button(window, text="Enviar", command=enviar_dados)
enviar_button.grid(row=2, column=0, columnspan=2)'''

window.mainloop()