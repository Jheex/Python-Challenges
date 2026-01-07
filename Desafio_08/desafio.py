#Desafio: Sistema de Triagem Anidrol
#O Cenário: Você precisa registrar o peso de lotes químicos.
#O sistema deve aceitar apenas lotes que pesem entre 1kg e 10kg.
#Qualquer peso fora disso deve ser descartado com um aviso.
#O programa encerra quando você digita 0.
#O que o código deve exibir no final:
#A lista com todos os pesos que foram aceitos.
#O peso total acumulado desses lotes aceitos.
pesos = []
total = 0

while True:
    print("Digite 0 para finalizar o sistema!")
    peso = float(input("Digite o peso em kg: "))

    if peso == 0:
        break
    elif peso > 10:
        print("Valor inválido")
    elif peso < 0:
        print("Valor inválido")
    else:
        pesos.append(peso)
        total = total + peso
        print("Lista dos pesos:", pesos)
        print("Soma total dos pesos:",total)
        continue
        