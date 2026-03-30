# Desafio_58

while True:
    funcionou = False

    try:
        print("-------------------------")
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
        funcionou = True
        print("-------------------------")
    except ValueError:
        print("Erro: digite apenas números!")
        funcionou = False
        print("")

    

    if funcionou == True:
        print("-------------------------")
        print("        OPERAÇÃO         ")
        print("-------------------------")
        print("1 - Somar                ")
        print("2 - Subtrair             ")
        print("3 - multiplicar          ")
        print("4 - Dividir              ")
        print("-------------------------")

        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            print("-------------------------")
            print("SOMANDO")
            soma = n1 + n2
            print(f"A soma é: {soma}")
        elif opcao == 2:
            print("-------------------------")
            print("SUBTRAINDO")
            sub = n1 - n2
            print(f"A subtração é: {sub}")
        elif opcao == 3:
            print("-------------------------")
            print("MULTIPLICANDO")
            mult = n1 * n2
            print(f"A multiplicação é: {mult}")
        elif opcao == 4:
            print("-------------------------")
            print("DIVIDINDO")
            div = n1 / n2
            print(f"A divisão é: {div}")
        else:
            print("Deu ruim")