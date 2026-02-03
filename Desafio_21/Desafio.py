tarefas = []

while True:
    print("1.Add, 2.Listar, 3.Remover (por índice), 4.Pesquisar, 5.Sair")
    try:
        opcao = (int(input("Digite o número: ")))
    except ValueError:
        print("Erro! Só é permitido números de 1 a 4")
        
    if opcao == 1:
        print("Adicionar")
        task = (str(input("Qual tarefa deseja adicionar? ")))
        tarefas.append(task)
        print("Sua lista de tarefas: ", tarefas)
        print("")
    elif opcao == 2:
            print("Listar")

            
# 1. Crie uma lista vazia para armazenar as tarefas
# 2. Inicie o loop principal do programa
    # 3. Exiba o menu: 1.Add, 2.Listar, 3.Remover (por índice), 4.Pesquisar, 5.Sair
    # 4. Receba a opção do usuário com tratamento de erro (try/except)
    # 5. Lógica da Opção 1 (Adicionar):
    #    - Receba o nome da tarefa e adicione à lista (.append)
    # 6. Lógica da Opção 2 (Listar):
    #    - Se a lista estiver vazia, avise.
    #    - Se não, percorra a lista mostrando o índice e a tarefa (Dica: use enumerate)

    # 7. Lógica da Opção 3 (Remover por Número):
    #    - Peça o número da tarefa.
    #    - Lembre-se: o usuário vê "1", mas o índice na lista começa em "0".
    #    - Use o método .pop(indice) para remover.
    #    - Trate erros caso o número não exista na lista.

    # 8. Lógica da Opção 4 (Pesquisar):
    #    - Peça um termo de busca.
    #    - Verifique se o termo está na lista (Operador 'in').

    # 9. Lógica da Opção 5 (Sair):
    #    - Encerre o loop.