tickets = []
qtd = 0

while True:
    print("Sistema de Tickets")
    print("")
    print("1 - Abrir ticket")
    print("2 - Ver ticket")
    print("3 - Sair")

    opcao = (int(input("Escolha uma opção: ")))

    if opcao == 1:
        print("")
        print("-----Abrindo Ticket-----")
        usuario = (str(input("Qual o nome do usuário? ")))

        if usuario == "":
            print("Resposta inválida!")
        else:
            print("")

        problema = (input("Qual o problema? "))
        if problema == "":
            print("Resposta inválida!")
        else:
            print("")

        status = "aberto"

        print("Ticket criado com sucesso!")
        qtd = qtd + 1

        tickets.append([
            {"usuario": usuario, 
             "problema": problema, 
             "status": status}
        ])

        print(f"{usuario} - {problema} - {status}")

    elif opcao == 2:
        print("")
        print("-----Visualizando Ticket-----")

        for i in range (1, qtd):
            print(f"Ticket {i} - {tickets}")
            print("")

    elif opcao == 3:
        print("")
        print("-----Saindo-----")
        break
    else:
        print("")
        print("Resposta inválida")