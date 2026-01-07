# 1. Mantenha seu cardápio e carrinho.
# 2. No menu de opções, adicione: [C]omprar, [L]impar Carrinho, [R]emover Item, [S]air.

# 3. Se for 'L':
#    - Use o comando carrinho.clear() para esvaziar tudo.

# 4. Se for 'R':
#    - Peça o nome do produto para remover.
#    - Se ele estiver no carrinho, use o 'del'.

#5. Adicionei o campo de visualizar carrinho

# 6. NA HORA DE MOSTRAR O PREÇO FINAL:
#    - Use f"R$ {valor:.2f}" para o Python colocar sempre dois números após a vírgula.

cardapio = {"coxinha":5.0, "suco":4.0, "pao":1.5}
carrinho = {}
total_geral = 0

print("")
print("Seja bem vindo a nossa padaria!")
print("")

while True:
    print("-----------Menu-----------")
    print("[C]omprar, [V]isualizar Carrinho, [L]impar Carrinho, [R]emover Item, [F]inalizar Compras, [S]air")
    opcao = (str(input("Qual opção você deseja? ").upper()))
    
    if opcao == "C":
            print("")
            print("Cardápio: ", cardapio)
            print("")
            produto = (str(input("Qual produto você deseja? ".lower()))) 
            
            if produto in cardapio:
                print("")
                print("Cardápio: ", cardapio)
                quantidade = int(input(f"Quantos {produto} você deseja? "))
                carrinho[produto] = carrinho.get(produto, 0) + quantidade
                print("Adicionado ao carrinho!")
                print("Seu carrinho: ",carrinho)
                print("")

            else:
                print("Não temos este produto no cardápio!")

    elif opcao =="L":
         carrinho.clear()
         print("Carrinho limpo")
         print("Carrinho: ", carrinho)

    elif opcao == "V":
         print("Visulizar carrinho:")
         print(carrinho)

    
    elif opcao == "R":
         print("Remover item do carrinho:")
         print("Carrinho: ", carrinho)
         remover = (str(input("Selecione o item que deseja excluir do carrinho: ")))
         del carrinho[remover]
         print("Produto removido com sucesso!")
         print("Carrinho atual: ",carrinho)
    
    elif opcao == "F":
        print("Finalizando Compra...")
        break

    elif opcao == "S":
        print("Saindo do Sistema...")
        break

for produto, quantidade in carrinho.items():
    preco = cardapio[produto]
    subtotal = preco * quantidade
    total_geral = subtotal + total_geral
        
    print("")
    print("Carrinho:", carrinho)
    print(f"Valor total: R${total_geral:.2f}")
    print("")
        

