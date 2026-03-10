carrinho = []

while True:
    print("")
    print("-----Meu carrinho-----")
    r1 = input("Digite um item: ")

    if r1 in carrinho:
        print("Já existe este item no carrinho!")
    elif r1 == "":
        print("Resposta inválida")
    else:
        carrinho.append(r1)
        print("Item adicionado ao carrinho!")
    print("")

    #---------------------------------------------#

    r2 = input("Digite um segundo item: ")

    if r2 in carrinho:
        print("Já existe este item no carrinho!")
    elif r2 == "":
        print("Resposta inválida")
    else:
        carrinho.append(r2)
        print("Item adicionado ao carrinho!")
    print("")

    #---------------------------------------------#

    r3 = input("Digite um terceiro item: ")

    if r3 in carrinho:
        print("Já existe este item no carrinho!")
    elif r3 == "":
        print("Resposta inválida")
    else:
        carrinho.append(r3)
        print("Item adicionado ao carrinho!")
    print("")

    #---------------------------------------------#

    r4 = input("Digite um quarto item: ")

    if r4 in carrinho:
        print("Já existe este item no carrinho!")
    elif r4 == "":
        print("Resposta inválida")
    else:
        carrinho.append(r4)
        print("Item adicionado ao carrinho!")
    print("")

    #---------------------------------------------#

    r5 = input("Digite um quinto item: ")

    if r5 in carrinho:
        print("Já existe este item no carrinho!")
    elif r5 == "":
        print("Resposta inválida")
    else:
        carrinho.append(r5)
        print("Item adicionado ao carrinho!")
    print("")

    print(f"Meu carrinho: {carrinho}")
    print("")
    break

#Modo 2

carrinhos = []

while True:
    print("--------------------")
    print("Sistema V2.0!")
    print("Meu carrinho")
    print("--------------------")
    print("")
    

    for i in range (1,6):
        item = input("Digite um item: ")
        if item in carrinhos:
            print(f"Já existe {item} na lista")
        elif item == "":
            print("Resposta inválida")
        else:
            carrinhos.append(item)
            print("Item adicionado ao carrinho!")
            print("")
            print(f"Meu carrinho: {carrinhos}")
    

