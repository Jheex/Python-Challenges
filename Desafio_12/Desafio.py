#1. Criar um dicionário chamado 'estoque' com 3 produtos e quantidades (ex: "chave": 10)
#2. Iniciar o loop 'while True:'
#3. Pedir o nome da peça para o usuário (Dica: use .lower() no final do input)
#4. Criar a condição de saída: se o usuário digitar "sair", use o 'break'
#5. AGORA O DESAFIO: 
#   - Use o comando 'in' para verificar se a peça digitada existe nas chaves do dicionário
#   - SE existir: Imprima a quantidade que está lá dentro (Dica: estoque[peca])
#   - SENÃO: Informe que a peça não existe
#6. No final, mostre uma mensagem de "Sistema de consulta encerrado"

estoque = {"chave": 10, "celular": 2, "tv": 8}

while True:
    print("Seja bem vindo ao sistema")
    print("Para sair do sistema, digite 'sair'")
    produto = str(input("Qual produto deseja pesquisar? ")).lower()
    print("")
    
    if produto == "sair":
        print("Saindo do Sistema!")
        print("")
        break
    elif produto in estoque:
        quantidade = estoque[produto]
        print(f"Há {quantidade} {produto} no inventário")
        print("Sistema de consulta encerrado")
        print("")
    else:
        print(f"Não há nenhum {produto} no estoque")
        print("Sistema de consulta encerrado")
        print("")