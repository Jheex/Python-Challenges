tarefas = []


while True:
    print("======================")
    print("         Menu         ")
    print("======================")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")
    print("5 - Marcar como concluída")
    print("======================")

    opcao = input("Escolha uma opção: ")
    print("")

    if opcao == "1":    
        print("Adicionar Tarefas")
        adicionar = input("Digite a tarefa: ")
        tarefas.append(adicionar)
        print("Tarefa adicionada com sucesso!")
        print("")

    elif opcao == "2":  
        print("Visualizar Tarefas")
        print(tarefas)
        print("")
    
    elif opcao == "3":  
        print("Remover Tarefas")
        remover = input("Qual tarefa deseja remover? ")
        print(tarefas)
        if remover in tarefas:
            tarefas.remove(remover)
            print("Tarefa removida com sucesso!")
            print("")
        else:
            print(f"Não consta nenhum {remover} na lista")

    elif opcao == "4":
        print("Saindo do Sistema")
        print("")
        break

    elif opcao == "5":
        print("Bônus - Marcar tarefa como concluída")
        print(tarefas)
        concluir = input("Qual tarefa deseja concluir? ")
        if concluir in tarefas:
            tarefas.append("✅")
            print("Tarefa concluída!")
        else:
            print(f"Não consta nenhum(a) {concluir} na lista")
    else:
        print("Opção inválida")

