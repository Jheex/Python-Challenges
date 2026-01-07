#Desafio: Ranking de Solo
#1. Pedir o nome do técnico (input de texto).
#2. Rodar o sistema de pH que você já criou.
#3. Ao sair do loop (após o break), criar um dicionário chamado 'relatorio'.
#4. O dicionário deve ter duas chaves: "tecnico" e "media".
#5. Imprimir o relatório final.



tecnico = []
amostras = []
soma = 0
media = 0

tecnico = str(input("Qual seu nome? "))
print("Seja bem-vindo ao sistema de PH")
print("Para finalizar o sistema, digite um valor negativo!")

while True:

    valor = float(input("Digite o valor (ph): "))
    
    if valor < 0:
        print(f"O técnico {tecnico} resultou na média {media:.2f}")
        print("Sistema desligado!")
        break
    elif valor >= 4 and valor <= 7:
        amostras.append(valor)
        soma = soma + valor
        media = soma / len(amostras)
        print("Lista de amostras aceitas: ", amostras)
        print("Quantidade de Amostras: ", len(amostras))
        print(f"A media dos valores é: {media:.2f}")

    elif valor > 7 or valor >= 0 and valor <= 3.9:
        print("Amostra descartada")
    else:
        print("")
    
        

