import tkinter as tk
from tkinter import Label
from tkinter import messagebox

def exibir_mensagem():
    # Recuperar informação digitada no Entry
    nome = campo.get()

    if nome != ():
        messagebox.showinfo(
            "Bem-vindo(a)!",
            f"Olá {nome}.Se você está vendo esta messangem, é porque você é um jovem apedeuta"
        )
    else:
        messagebox.showwarning(
            "Ops",
            "Primeiro você precisa digitar o seu NOME"
        )

# Criando uma janela
janela = tk.Tk()
# Inserindo título para uma janela criada
janela.title("Montando Interface com Python")
# Definindo dimensões
janela.geometry("600x400")

titulo = tk.Label(
    janela,
    text="Fala galera",
    font=("Arial",20)
).pack(pady=10)

botao = tk.Button(
    janela,
    text="Clique aqui",
    font=("Arial",16),
    command=exibir_mensagem
).pack(pady=10)

campo =  tk.Entry(
    janela,
    font=("Arial",12),
    width=20
)
campo.pack(pady=10)



# Executandr a janela Tkinter
janela.mainloop()

