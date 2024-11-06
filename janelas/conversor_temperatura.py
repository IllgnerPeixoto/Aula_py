import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("")

# entrada de texto
entry = tk.Entry(fg="black", bg="white", width=5)
entry.grid(row=0, column=0, sticky="wn")


# criando label F
label1 = tk.Label(window, text="°F", width=5, height=5)
label1.grid(row=0, column=1, sticky= "nw")





window.mainloop()

