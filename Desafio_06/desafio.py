#1. Crie uma variável 'total_vendas' começando com 0
#2. Inicie um loop 'while True:' (isso cria um loop infinito)
#3. Dentro do loop, peça o 'valor' de um produto (use float(input))
#4. Crie um 'if': se o 'valor' for igual a 0, use o comando 'break' para sair do loop
#5. Caso o valor não seja 0, some esse 'valor' à variável 'total_vendas'
#6. Fora do loop (depois que o usuário digitar 0), imprima o 'total_vendas'

total_vendas = 0

while True:
    valor = float(input("Digite um valor: "))
    if valor == 0:
        print("Total de vendas: ", total_vendas)
        break
    else:
        total_vendas = total_vendas + valor