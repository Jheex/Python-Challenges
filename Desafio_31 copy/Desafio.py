convidados = []

print("")
qtd = (int(input("Quantos convidados deseja convidar? ")))

while True:
    for i in range (qtd):
        print("")
        nome = (str(input("Digite o nome do convidado: ")))
        if nome == "":
            print("Reposta inválida, insira novamente")
        elif nome in convidados:
            print("Convidado já adicionado, insira novamente")
        else:
            convidados.append(nome)
            print("Convidado adicionado com sucesso!")
    print("")
    print("Lista final de convidados: ")
    print(convidados)
