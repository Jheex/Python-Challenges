# Desafio_49
import json

def adicionar_produto():
    print("")
    print("ADICIONANDO PRODUTO")
    id = 1
    nome = str(input("Digite o produto: ").lower())
    preco = float(input("Digite o preço: R$ "))
    estoque = int(input("Digite a quantidade: "))

    cadastro = {
        "id": id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    print("Resumo do produto:")
    print(f"Produto {nome} - Preço {preco} - Estoque {estoque}")

    with open ("Desafio_49/lojinha.json", "r") as arquivo:
        dados = json.load(arquivo)
    
    dados.append(cadastro)

    with open ("Desafio_49/lojinha.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Produto inserido com sucesso!")
    print(dados)

def visualizar_produto():
    print("")
    print("LISTANDO PRODUTOS")
    with open ("Desafio_49/lojinha.json", "r") as arquivo:
        dados = json.load(arquivo)

    print(dados)

def remover_produto():
    print("")
    print("REMOVENDO PRODUTO")

    achou = False

    with open ("Desafio_49/lojinha.json", "r") as arquivo:
        dados = json.load(arquivo)

    print("Lista de Produtos:")
    print(dados)
    id = int(input("Digite o ID do produto que deseja remover: "))

    for item in dados:
        if item["id"] == id:
            print("Id encontrado")
            achou = True
            dados.remove(item)
        
    if achou == True:
        with open ("Desafio_49/lojinha.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("Produto Removido!")
        print("Lista Atual", dados)

    else:
        print("Produto inexistente!")
        
def editar_produto():

    with open ("Desafio_49/lojinha.json", "r") as arquivo:
        dados = json.load(arquivo)

    print("")
    print("EDITANDO PRODUTOS")
    print(dados)

    achou = False

    print("")
    id = int(input("Digite o ID do produto que deseja alterar: "))

    for item in dados:
        if item["id"] == id:
            print("Produto Encontrado")
            print("")
            achou = True

    if achou:
        print("ALTERANDO ITEM")

        novo_nome = input("Digite o novo nome do produto: ")
        novo_preco = float(input("Digite o novo preço do produto: R$ "))
        novo_estoque = int(input("Digite a nova quantidade do produto: "))

        item["nome"] = novo_nome
        item["preco"] = novo_preco
        item["estoque"] = novo_estoque

        with open ("Desafio_49/lojinha.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        print("LISTA DE PRODUTOS:")
        print(dados)

    else:
        print("")
        print("Produto não existente")
        editar_produto()
        print("")

def buscar_produto():
    print("SEI NAO")

def calcular_estoque():
    print("")
    print("CALCULANDO ESTOQUE")

    with open("Desafio_49/lojinha.json", "r") as arquivo:
        dados = json.load(arquivo)

    total = 0

    for item in dados:
        total += item["preco"] * item["estoque"]

    print(f"Valor total do estoque: R$ {total:.2f}")

    

while True:
    print("")
    print("-----------------------")
    print("    LOJINHA DO JHON    ")
    print("-----------------------")
    print("1 - Adicionar Produtos" )
    print("2 - Listar Produtos"    )
    print("3 - Remover Produtos"   )
    print("4 - Editar Produtos"    )
    print("5 - Buscar Produtos"    )
    print("6 - Calcular Estoque"   )
    print("7 - Sair do Sistema"    )
    print("")
    opcao = int(input("Selecione uma opção: "))
    print("")

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        visualizar_produto()
    elif opcao == 3:
        remover_produto()
    elif opcao == 4:
        editar_produto()
    elif opcao == 5:
        buscar_produto()
    elif opcao == 6:
        calcular_estoque()
    elif opcao == 7:
        print("Saindo do Sistema...")
        break
    else:
        print("Opção inválida")