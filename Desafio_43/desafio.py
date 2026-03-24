lista = [
    {"nome": "refrigerante", "preco": 0.0, "estoque": 0}
]

while True:
    print("")
    print("-----MENU-----")
    print("1 - Listar produtos")
    print("2 - Adicionar produto")
    print("3 - Alterar preço")
    print("4 - Alterar estoque")
    print("0 - Sair")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        print("")
        print("-----LISTAR PRODUTOS-----")
        print("Lista:", lista)

    elif opcao == 2:
        print("")
        print("-----ADICIONAR PRODUTOS-----")
        nome = str(input("Escreva o nome do produto: ").lower())
        preco = float(input("Escreva o preço do produto: R$ "))
        estoque = int(input("Escreva a quantidade do produto: "))

        existe = False

        # Percorre todos os produtos para ver se já existe
        for item in lista:
            if item["nome"] == nome:
                existe = True
                break  # achou, para de procurar

        if existe:
            print("Já existe este produto no sistema!")
        else:
            lista.append({"nome": nome, "preco": preco, "estoque": estoque})
            print("Item adicionado com sucesso!")
            print("Lista:", lista)

    elif opcao == 3:
        print("")
        print("-----ALTERAR PREÇO-----")
        print("Lista:", lista)
        nome = str(input("Escreva o nome do produto: ").lower())

        achou = False

        for item in lista:
            if item["nome"] == nome:
                print("Produto encontrado!")
                preco = float(input("Escreva o preço do produto: R$ "))
                item["preco"] = preco
                print("Alteração finalizada com sucesso!")
                print("Lista:", lista)
                achou = True
                break

        if not achou:
            print("Produto não encontrado")

    elif opcao == 4:
        print("")
        print("-----ALTERAR ESTOQUE-----")
        print("Lista:", lista)

        achou = False

        nome = str(input("Escreva o nome do produto: ").lower())
        for item in lista:
            if item["nome"] == nome:
                print("Produto encontrado!")
                estoque = int(input("Escreva a quantidade do produto: "))
                item["estoque"] = estoque
                print("Alteração finalizada com sucesso!")
                print("Lista:", lista)
                achou = True
                break
        if not achou:
                print("Produto não encontrado!")

    elif opcao == 0:
        print("")
        print("-----SAINDO DO SISTEMA-----")
        break
    else:
        print("")
        print("Opção Inválida")