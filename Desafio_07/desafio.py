#1. Crie uma lista vazia chamada 'historico' (ex: historico = [])
#2. Inicie o loop 'while True:'
#3. Peça o 'valor' (float input)
#4. Se o valor for 0, dê o 'break'
#5. Se não for 0, use o 'historico.append(valor)' para salvar na lista
#6. Fora do loop, imprima a frase "Seu extrato:" e depois imprima a lista 'historico'

historico = []

while True:
    valor = float(input("Digite o valor: "))
    if valor == 0:
        break
    else:
        historico.append(valor)

print("Seu extrato:", historico )