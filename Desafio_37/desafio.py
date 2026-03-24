lista = []

for i in range (0,5):
    resposta = int(input("Digite um número: "))
    lista.append(resposta)

print("Lista: ",lista)

maior = max(lista)
menor = min(lista)

print(f"O maior é {maior}")
print(f"O menor é {menor}")