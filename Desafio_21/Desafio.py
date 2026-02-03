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

#funcionalidades necessárias:
#Exibir Saldo: Mostrar quanto dinheiro há na conta (comece com um valor inicial, ex: R$ 1000).
#Depósito: Somar um valor ao saldo atual.
#Saque: Subtrair um valor do saldo, mas atenção: não pode permitir que o saldo fique negativo.
#Sair: Encerrar o programa.

#Requisitos Técnicos:
#Use um loop while True para manter o menu ativo.
#Use input() para ler os comandos do usuário.
#Trate o erro de "Saldo Insuficiente" no momento do saque.

#Exemplo de como o menu deve aparecer:
#Plaintext

#---------- BANCO PYTHON ----------
#1. Consultar Saldo
#2. Depósito
#3. Saque
#4. Sair
#----------------------------------
#Escolha uma opção:

saldo = 1000.00

while True:
    print("---------- BANCO PYTHON ----------")
    print("1. Consultar Saldo")
    print("2. Depósito")
    print("3. Saque")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("")
        print("----------SALDO----------")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        print("")
    elif opcao == 2:
        print("----------DEPÓSITO----------")
        print("Quanto deseja depositar?")
        deposito = (float(input("Insira o valor: ")))
        saldo = saldo + deposito
        print(f"Seu saldo atual é {saldo:.2f}")
    elif opcao == 3:
        print("----------SAQUE----------")
        print("Quanto deseja sacar?")
        saque = (float(input("Insira o valor: ")))
        if saque <= saldo and saldo > 0:
            saldo = saldo - saque
            print(f"Seu saldo atual é {saldo:.2f}")
        else:
            print("Saldo Insuficiente")
    elif opcao == 4:
        print("----------FINALIZANDO----------")
        print("Sistema finalizado com sucesso!")
        break
    else:
        print("Esta opção não existe")
