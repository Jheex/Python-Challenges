#01. Criar o dicionário 'precos' com os 3 itens e seus valores (float)
#02. Iniciar o 'while True:'
#03. Pedir o nome do produto ou 'fim' para sair (.lower)
#04. SE o produto for 'fim': break
#05. SE o produto existir no dicionário:
#06. Pedir a quantidade (int)
#07. Calcular subtotal = precos[produto] * quantidade
#08. SE subtotal > 20:
#09. Calcular total_com_desconto = subtotal * 0.90
#10. Exibir o valor com desconto (f-string :.2f)
#11. SENAO:
#12. Exibir o subtotal normal (f-string :.2f)
#13. SENAO:
#14. Exibir "Produto não encontrado"

precos = {"pao": 0.50, "leite": 4.50, "cafe": 12.00}
subtotal = 0

print("")
print("Bem vindo ao sistema!")
print("Para sair do sistema, digite: 'fim'.")
print("")

while True:
    produto = str(input("Qual produto você deseja? " )).lower()
    if produto == "fim":
        print("Saindo do sistema...")
        print("")
        break

    elif produto in precos:
            quantidade = (float(input("Qual a quantidade? ")))
            subtotal = precos[produto] * quantidade
            
            if subtotal > 20.0:
                desconto = subtotal * 0.1
                total = subtotal - desconto
                print("Subtotal:", subtotal)
                print("Desconto:", desconto)
                print(f"O valor final é de {total}!")
                print("Finalizando sistema!")
                break
            else:
                 print(f"O valor final é {subtotal}.")
                 break
    else:
        print("Produto não foi cadastrado!")

