
# 1. Crie o dicionário 'cardapio' com: coxinha (5.0), suco (4.0) e pao (1.5)
# 2. Crie um dicionário VAZIO chamado 'carrinho'

# 3. Inicie um loop 'while True':
#    - Imprima o cardápio para o usuário ver os nomes e preços
#    - Peça o nome do item que ele quer comprar (ou 'sair' para fechar)
#    - SE o usuário digitar 'sair':
#        - Dê um break

#    - SE o item digitado ESTIVER no 'cardapio':
#        - Peça a QUANTIDADE desse item (use int)
#        
#        - AGORA A MÁGICA DO .GET:
#        - No dicionário 'carrinho', a chave será o NOME do item.
#        - O valor será: o que já tinha lá (use .get(item, 0)) + a nova quantidade.
#        - Ex: carrinho[item] = carrinho.get(item, 0) + quantidade
#        
#        - Imprima: "Adicionado ao carrinho!"
#    - SENÃO:
#        - Imprima: "Produto não temos no cardápio."

# 4. FORA DO LOOP (O fechamento da conta):
#    - Crie uma variável 'total_geral = 0'
#    - Use um 'for item, qtd in carrinho.items():'
#        - Pegue o preço unitário lá no dicionário 'cardapio'
#        - Calcule o subtotal (quantidade * preço)
#        - Some o subtotal ao 'total_geral'
#        - Imprima: f"{item} - Qtd: {qtd} - Subtotal: R${subtotal}"

# 5. Imprima o VALOR TOTAL DA COMPRA

cardapio = {"coxinha":5.0, "suco":4.0, "pao":1.5}
carrinho = {}
total_geral = 0

print("")
print("Seja bem vindo a nossa padaria!")
print("")
print("Para sair do sistema, digite: 'sair'")

while True:
    print("Cardápio: ", cardapio)
    print("")
    produto = (str(input("Qual produto você deseja?".lower()))) 
    if produto == "sair":
        print("Saindo do Sistema...")
        break
    elif produto in cardapio:
        print("")
        print("Cardápio: ", cardapio)
        quantidade = int(input(f"Quantos {produto} você deseja? "))
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        print("Adicionado ao carrinho!")
        print("Seu carrinho: ",carrinho)
        print("")
    else:
        print("Não temos este produto no cardápio!")

for produto, quantidade in carrinho.items():
    preco = cardapio[produto]
    subtotal = preco * quantidade
    total_geral = subtotal + total_geral
    
print("")
print("Carrinho", carrinho)
print("Valor total: ", total_geral)
print("")