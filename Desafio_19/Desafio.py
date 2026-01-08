# Primeiro, crie uma variável para guardar o dinheiro total do usuário
# Agora, comece um ciclo que não para até que o usuário decida sair
    # Mostre na tela quanto dinheiro ele tem no momento
    # Mostre as opções: 1-Depositar, 2-Sacar, 3-Sair
    # Crie uma variável para receber o que o usuário digitar no teclado

    # Se a escolha for igual a "1" (Depósito):
        # Pergunte o valor (não esqueça de converter para número decimal!)
        # Atualize a variável do saldo somando esse valor
        # Mostre uma mensagem de confirmação

    # Se a escolha for igual a "2" (Saque):
        # Pergunte quanto ele quer tirar
        # Verifique: O valor pedido é menor ou igual ao que ele tem?
            # Se sim, subtraia do saldo e confirme
            # Se não, avise que o saldo é insuficiente
    # Se a escolha for igual a "3" (Sair):
        # Mude a condição do ciclo para ele encerrar
        # Diga "Até logo"
        
    # Se ele digitar qualquer outra coisa:
        # Avise que a opção não existe

saldo = 1200.00

print("")
print("Bem vindo ao nosso banco!")

while True:
    print(f"Este é seu saldo {saldo:.2f}")
    print("")
    print("1-Depositar, 2-Sacar, 3-Sair")
    try:
        opcao = (int(input("Selecione a opção desejada: ")))
    except ValueError:
        print("Ei, digite apenas números!")
        continue
    print("")
    if opcao == 1:
        print("Qual valor deseja depositar?")
        depositar = (float(input("Inserir valor: ")))
        saldo = saldo + depositar
        print("Depósito concluído!")
        print(f"Saldo atual {saldo:.2f}")
        print("")
    elif opcao == 2:
        print("Qual valor deseja sacar?")
        sacar = (float(input("Inserir valor: ")))
        if sacar <= saldo:
            saldo = saldo - sacar
            print("Saque concluido com sucesso!")
            print(f"Seu saldo atual é: {saldo:.2f}")
        else:
            print("Saldo insuficiente")
    elif opcao == 3:
        print("Até logo")
        break
    else:
        print("Opção inexistente")





            
