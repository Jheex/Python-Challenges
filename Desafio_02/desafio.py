# 1. Crie uma lista chamada 'vendas' com os valores: 2000, 4500, 1200
# 2. Inicie um laço 'for' para percorrer cada 'valor' dentro da lista 'vendas'
# 3. Crie um 'if' que verifica se o 'valor' é maior ou igual a 3000
# 4. Se for verdade, imprima: "Ganhou bônus: " e o valor
# 5. Crie o 'else' (caso o valor seja menor que 3000) 
# 6. Imprima: "Sem bônus: " e o valor

vendas = [2000, 4500, 1200]

for i in vendas:
    if i >= 3000:
        print("Ganhou bônus", i)
    else:
        print("Sem bônus", i)