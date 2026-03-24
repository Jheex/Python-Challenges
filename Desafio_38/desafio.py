# Desafio_38
valores = []

for i in range (0,6):
    resposta = int(input("Digite um número: "))
    valores.append(resposta)

maior = max(valores)
menor = min(valores)

print("LISTA: ", valores)
print("O maior da lista é: ", maior)
print("O menor da lista é: ", menor)