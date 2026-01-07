#01. Pedir o nome do Operador (input)
#02. Criar uma lista vazia para as temperaturas aceitas
#03. Iniciar o loop 'while True:'
#04. Iniciar o bloco 'try:' (para capturar erros de digitação)
#05. Pedir a temperatura (float input)
#06. Verificar se é 999 para dar 'break'
#07. Se a temperatura estiver entre 15 e 28 (inclusive):
#08. Adicionar à lista de aceitas
#09. Caso contrário (else):
#10. Exibir alerta de temperatura fora da faixa
#11. Criar o 'except ValueError:' (caso digitem letras)
#12. Exibir mensagem de erro de digitação
#13. FORA DO LOOP:
#14. Calcular a média (se a lista não estiver vazia)
#15. Criar o dicionário 'dados_estufa' com: operador, quantidade e media
#16. Imprimir o dicionário final
temperaturas = []
soma = 0
media = 0

operador = str(input("Qual seu nome? "))
print("Para finalizar o sistema, digite: 999")
print("Seja bem vindo ao nosso sistema!")

while True:
    try:
        valor = int(input("Digite a temperatura: "))
    except:
        print("Erro! Deve-se digitar um número!")
        continue
    if valor == 999:
        print("Dicionário: ", dados_estufa)
        break
    elif valor >= 15 and valor <= 28:
        temperaturas.append(valor)
        soma = soma + valor
        quantidade = len(temperaturas)
        media = soma/quantidade
        dados_estufa = {operador}, {quantidade}, {media}

        print("Lista das temperaturas: ", temperaturas)
        print("A soma total das temperaturas: ", soma)
        print("A quantidade total de temperaturas: ", quantidade)
        print("A media total das temperaturas: ", media)

    else:
        print("Temperatura fora da faixa!")
