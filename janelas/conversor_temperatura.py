import tkinter as tk

def fahrenheit_para_celsius():
    fahrenheit = entry.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    label2["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("conversor de temperatura")
window.resizable(width=False, height=False)

# entrada de texto
entry = tk.Entry(master = window, fg="black", bg="white", width=5)
entry.grid(row=0, column=0, sticky="e")


# criando label F
label1 = tk.Label(master = window, text="°F", width=5, height=5)
label1.grid(pady=10, row=0, column=1,sticky= "w" )

#criando botão
button = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_para_celsius)
button.grid(pady=10, row=0, column=3, sticky= "w")

#resultado 
label2 = tk.Label(master = window, text="°C", width=5, height=5)
label2.grid(pady=10, row=0, column=4,sticky= "w" )
                   





window.mainloop()

