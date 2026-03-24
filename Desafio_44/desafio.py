import tkinter as tk

janela = tk.Tk()
janela.title("O nome ta certo")
janela.geometry("3000x1000")

entrada = tk.Entry(janela)
entrada.pack(pady=100)

def mostrar_texto():
    texto = entrada.get
    print("Você digitou ", texto)

botao = tk.Button(janela, text="Mostrar texto", command=mostrar_texto)
botao.pack()





janela.mainloop()