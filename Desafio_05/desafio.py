#1. Crie uma variável 'valor_produto' que recebe um input do usuário
#Dica: Use float(input("Digite o valor: ")) para poder digitar números com ponto
#2. Crie uma variável 'taxa' com o valor 0.10 (isso representa 10%)
#3. Crie uma variável 'valor_imposto' que é o 'valor_produto' multiplicado pela 'taxa'
#4. Crie uma variável 'total' que é a soma do 'valor_produto' + 'valor_imposto'
#5. Imprima: "O valor do imposto é: " e o valor_imposto
#6. Imprima: "O total a pagar é: " e o total

valor_produto = float(input("Digite o valor: "))
taxa = 0.10
valor_imposto = valor_produto * taxa
total = (valor_produto + valor_imposto)

print("O valor do imposto é:", valor_imposto)
print("O total a pagar é:", total)


