# 1. Crie o dicionário 'produtos' com mouse, teclado e monitor e seus preços
# 2. SE a opção for 'A':
#    - Peça o nome do novo produto
#    - Peça o preço (use float)
#    - Adicione ao dicionário usando: produtos[nome] = preco
#    - Imprima uma mensagem de sucesso
# 3. SENÃO SE (elif) a opção for 'U':
#    - Peça o nome do produto que o usuário quer mudar o preço
#    - SE o nome digitado ESTIVER (in) no dicionário produtos:
#        - Peça o novo preço
#        - Atualize usando: produtos[nome] = novo_preco
#    - SENÃO:
#        - Avise que o produto não foi encontrado
# 4. SENÃO SE (elif) a opção for 'R':
#    - Peça o nome do produto para remover
#    - SE o nome ESTIVER (in) no dicionário produtos:
#        - Delete usando: del produtos[nome]
#        - Avise que foi removido
#    - SENÃO:
#        - Avise que o produto não existe

# 5. SENÃO:
#    - Imprima "Opção Inválida"

# 6. Fora de todos os IFs, imprima o dicionário final para ver o resultado


produtos = {"mouse":30.50, "teclado":100.50, "monitor":200.00}

print("")
print("--- SISTEMA DE ESTOQUE ---")
print("")
print("Opções: [A]dicionar, [E]ditar, [R]emover")
opcao = input("O que deseja fazer? ").upper()

if opcao == "A": #cadastro de produtos
    print("")
    print("Adicionando Produtos:")
    produto= (str(input("Qual o nome do novo produto? ")))
    preco = (float(input("Qual o preço do produto? " )))
    produtos[produto] = preco
    print("Produto cadastrado com sucesso!")
    print("")


elif opcao == "E":
    print("")
    print("Editando Produtos:")
    print(f"Lista de produtos: {produtos}")
    editar = (str(input("Qual produto deseja editar? ")))
    if editar in produtos:
        preco = float(input(f"Qual o novo preço do {editar}? "))
        produtos[editar] = preco
        print("")
    else:
        print("Produto não encontrado")
        print("")

elif opcao == "R":
    print("")
    print("Removendo Produtos:")
    print(f"Produtos: {produtos}")
    remover = (str(input("Qual produto deseja remover? ")))
    if remover in produtos:
        del produtos[remover]
        print("")
        print(f"O produto {remover} foi removido!")
        print("")
    else:
        print("Produto não existe")
else:
    print("Opção inválida")
            
print("Lista de Produtos: ", produtos)

