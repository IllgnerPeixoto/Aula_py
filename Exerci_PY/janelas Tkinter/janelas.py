import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("600x500")

# Criação de um rótulo
label = tk.Label(janela, text="Olá, Tkinter!",  
                foreground="white",  # Define a cor do texto # pode abreviar para fg (foreground)
                background="black", # Define a cor do fundo # pode abreviar para bg (background)
                width= 10, #Define largura
                height= 3 #Define altura
                )
                
                
label.pack(pady=10) # pady serve para dar margem aos botões

# Criação de um botão
button = tk.Button(janela, text="Clique Aqui, para ganhar no tigrinho", 
                    foreground="white",
                    background="green", 
                    #width=50, 
                    #height=10, 
                    command=lambda: label.config(text="ganhou!"))
button.pack(pady=10)

# Adicionando uma entrada no texto
entry = tk.Entry(fg="black", bg="white", width=50)
entry.pack(pady=10)

# Criando outro botão
button2 = tk.Button( janela,
                    text="Escreva algo e clique no botão",
                    command = lambda: label.config(text= entry.get()))
button2.pack(pady= 10)

button3 =tk.Button (janela, text= "Apagar",
                    fg = "white",
                    bg = "red",
                    command=lambda: label.config(text=""))
button3.pack(pady= 10)

# Iniciando o loop principal
janela.mainloop()

