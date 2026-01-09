#funcionalidades necessárias:
#Exibir Saldo: Mostrar quanto dinheiro há na conta (comece com um valor inicial, ex: R$ 1000).
#Depósito: Somar um valor ao saldo atual.
#Saque: Subtrair um valor do saldo, mas atenção: não pode permitir que o saldo fique negativo.
#Sair: Encerrar o programa.

#Requisitos Técnicos:
#Use um loop while True para manter o menu ativo.
#Use input() para ler os comandos do usuário.
#Trate o erro de "Saldo Insuficiente" no momento do saque.

#Exemplo de como o menu deve aparecer:
#Plaintext

#---------- BANCO PYTHON ----------
#1. Consultar Saldo
#2. Depósito
#3. Saque
#4. Sair
#----------------------------------
#Escolha uma opção:

saldo = 1000.00

while True:
    print("---------- BANCO PYTHON ----------")
    print("1. Consultar Saldo")
    print("2. Depósito")
    print("3. Saque")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("")
        print("----------SALDO----------")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        print("")
    elif opcao == 2:
        print("----------DEPÓSITO----------")
        print("Quanto deseja depositar?")
        deposito = (float(input("Insira o valor: ")))
        saldo = saldo + deposito
        print(f"Seu saldo atual é {saldo:.2f}")
    elif opcao == 3:
        print("----------SAQUE----------")
        print("Quanto deseja sacar?")
        saque = (float(input("Insira o valor: ")))
        if saque <= saldo and saldo > 0:
            saldo = saldo - saque
            print(f"Seu saldo atual é {saldo:.2f}")
        else:
            print("Saldo Insuficiente")
    elif opcao == 4:
        print("----------FINALIZANDO----------")
        print("Sistema finalizado com sucesso!")
        break
    else:
        print("Esta opção não existe")



