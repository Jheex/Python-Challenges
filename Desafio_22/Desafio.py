
# 1. Crie uma variável para armazenar a lista de compras (vazia)

# 2. Inicie um loop infinito para o menu principal

    # 3. Exiba o menu com as opções:
    # 1 - Adicionar
    # 2 - Remover
    # 3 - Exibir Lista
    # 4 - Sair

    # 4. Receba a escolha do usuário através de um input

    # 5. Verifique SE a opção for '1' (Adicionar):
        # Peça o nome do item ao usuário
        # Adicione o item à lista usando o método .append()
        # Exiba uma mensagem de confirmação
    # 6. OU SE a opção for '2' (Remover):
        # Peça o nome do item que deve ser removido
        # Verifique SE o item existe na lista (use o 'in')
            # Se existir, use o método .remove() para deletar
            # Mostre uma mensagem de sucesso
        # SENÃO (se não existir):
            # Mostre um aviso de que o item não foi encontrado
    # 7. OU SE a opção for '3' (Exibir Lista):
        # Verifique SE a lista está vazia (use o len())
            # Se estiver vazia, avise ao usuário
        # SENÃO:
            # Use um loop 'for' para mostrar cada item da lista individualmente
    # 8. OU SE a opção for '4' (Sair):
        # Exiba uma mensagem de despedida
        # Use o 'break' para encerrar o programa

    # 9. SENÃO (para qualquer outra entrada):
        # Informe que a opção é inválida

carrinho = []

while True:
    print("-----MENU-----")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Exibir Lista")
    print("4 - Sair")
    opcao = (int(input("Digite a sua opção: ")))
    if opcao == 1:
        adicionar = str(input("Qual o nome do produto? "))
        carrinho.append(adicionar)
        print("Seu produto foi adicionado ao carrinho")
        print(carrinho)
        print("")
    elif opcao == 2:
        remover = str(input("Qual o nome do produto? "))
        if remover in carrinho:
            carrinho.remove(remover)
            print("Produto removido com sucesso!")
            print(carrinho)
            print("")
        else:
            print("O item não foi encontrado")
    elif opcao == 3:
        if len(carrinho) > 0:
            print(carrinho)
        else:
            print("Sua lista está vazia")
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Erro, resposta inválida")
    
    
    









