# 1. Crie um dicionário chamado 'produtos'
#    Adicione: "celular" (1500), "fone" (200), "capinha" (50)
# 2. Peça para o usuário digitar o NOME do produto que ele quer consultar
#    Dica: use o .lower() para garantir que 'Celular' ou 'CELULAR' funcionem
# 3. Procure o preço desse produto no dicionário e guarde numa variável 'preco_base'
#    (Aqui é onde você treina a 'puxada' usando o nome que o usuário digitou)
# 4. Agora, peça para o usuário digitar quantos % de DESCONTO ele quer aplicar (0 a 100)
#    IMPORTANTE: Lembre-se que o input recebe texto, mas para cálculo você precisa de NÚMERO.
#    Dica: Use int() ou float()
# 5. Calcule o valor do desconto: (preco_base * porcentagem) / 100
# 6. Calcule o preço final (preco_base - desconto)
# 7. Imprima o resultado final mostrando:
#    "O produto [NOME] custava R$[VALOR] e com o desconto sai por R$[FINAL]"

produtos = {"celular":1500, "fone":200, "capinha":50}

resposta = (str(input("Digite o Nome do produto que deseja consultar: ").lower()))
preco_base = produtos[resposta]
print("Selecione o desconto! lembrando que o limite é de 0 a 100")
desconto = (int(input(f"Quantos % de desconto você quer aplicar no {resposta}? ")))
divisao = (desconto / 100)
mult = preco_base * divisao
valorfinal = preco_base - mult

print(f"O produto: {resposta} custava R${preco_base:.2f} e com o desconto sai por R${valorfinal:.2f}")


