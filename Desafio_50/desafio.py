import json

def adicionar_tarefas():
    tarefa = input("Qual tarefa deseja adicionar: ")
    
    with open ("Desafio_50/tarefas.json", "r") as arquivo:
        dados = json.load(arquivo)

    dados.append(tarefa)

    with open ("Desafio_50/tarefas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"Lista: {dados}")

def listar_tarefas():
    with open ("Desafio_50/tarefas.json", "r") as arquivo:
        dados = json.load(arquivo)

    for i in (0, dados):
        print(f"{i} - {dados}") 




while True:
    print("")
    print("--------------------------")
    print("    SISTEMA DE TAREFAS"    )
    print("--------------------------")
    print("1 - Adicionar tarefa"      )
    print("2 - Listar tarefas"        )
    print("3 - Remover tarefa"        )
    print("4 - Sair"                  )
    print("--------------------------")
    opcao = int(input("Selecione uma opção: "))
    print("")

    if opcao == 1:
        adicionar_tarefas()
    elif opcao == 2:
        listar_tarefas()