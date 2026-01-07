#Desafio: Analisador de Solo (pH)
#O Cenário: Você deve coletar amostras de pH de solo (escala de 0 a 14).
#1. Criar uma lista para as amostras aceitas.
#2. Iniciar um loop que só para se o usuário digitar um número NEGATIVO.
#3. Se o pH estiver entre 4.0 e 7.0 (inclusive), salvar na lista.
#4. Se o pH for maior que 7.0 ou entre 0 e 3.9, exibir "Amostra descartada".
#5. No final (fora do loop), exibir:
#   - A lista de amostras aceitas.
#   - A quantidade de amostras (use len).
#   - A média dos valores (soma / quantidade) usando f-string com :.2f.

amostras = []
soma = 0
media = 0

while True:
    print("Para finalizar o sistema, digite um valor negativo!")
    valor = float(input("Digite o valor (ph): "))
    
    if valor < 0:
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
        print("sei la kkkkk")
    
        

