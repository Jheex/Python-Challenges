# 1. Crie a função 'converter_dolar' que recebe um parâmetro (valor_dolar)
    # 2. Calcule o valor em reais (valor_dolar vezes 5)
    # 3. Use o return para devolver esse resultado em reais

def converter_dolar (valor_dolar):
    conversao = valor_dolar * 5
    return conversao

while True:
    money = float(input("Escreva o valor em USD para converter para R$: "))
    total_reais = converter_dolar(money)

    with open("Cambio.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Dolar: {money} | Real: {total_reais} \n")
    print(f"Dolar: {money} | Real: {total_reais} \n")

# --- CORPO PRINCIPAL ---

# 4. Crie um loop (while)
    
    # 5. Peça para o usuário digitar o valor em Dólar (float input)
    
    # 6. Chame a função e guarde o resultado dela numa variável chamada 'total_reais'
    
    # 7. Abra o arquivo 'cambio.txt' no modo de adicionar ("a")
    
        # 8. Escreva no arquivo: "Dolar: X | Real: Y" (pule linha)

    # 9. Print na tela para o usuário ver quanto deu a conversão