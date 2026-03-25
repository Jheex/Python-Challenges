# Desafio_48

import json

while True:
    print("------------")
    print("SISTEMA JSON")
    print("------------")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Visualizar")
    print("0 - Sair")
    print("------------")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("")
        print("ADICIONAR")

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        email = input("Digite seu e-mail: ")

        cadastro = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        with open ("Desafio_48/usuarios.json", "r") as arquivo:
            dados = json.load(arquivo)
        
        dados.append(cadastro)


        with open ("Desafio_48/usuarios.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        print("Dados inseridos com sucesso!")
        print(dados)

    elif opcao == 2:
        print("")
        print("REMOVER")

        remover = input("Qual usuário será removido? ")

        with open ("Desafio_48/usuarios.json", "r") as arquivo:
            dados = json.load(arquivo)

        achou = False

        for pessoa in dados:
            if pessoa["nome"] == remover:
                print("Usuario encontrado!")
                achou = True
                dados.remove(pessoa)
                break
            
        if achou:
            with open ("Desafio_48/usuarios.json", "w") as arquivo:
                json.dump(dados, arquivo, indent=4)

            print("Usuario removido com sucesso!")
            print(dados)

        else:
            print(f"Não há nenhum {remover} na lista")    

    elif opcao == 3:
        print("")
        print("VISUALIZAR")

        with open ("Desafio_48/usuarios.json", "r") as arquivo:
            dados = json.load(arquivo)
            
        print(dados)
        

    elif opcao == 0:
        print("")
        print("SAINDO...")
        break
    else:
        print("Opção Inválida")