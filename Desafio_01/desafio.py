#Você tem uma lista de números: dados = [150, 200, 50, 300, 80, 450, 100]
#O Desafio: Crie uma lógica que percorra essa lista e imprima apenas os valores que são maiores que 150.
#O que você vai precisar: Um laço de repetição (for) e uma condicional (if).

dados = [150, 200, 50, 300, 80, 450, 100]

for i in dados:
    if i > 150:
        print(f"Este é maior que 150 = {i}")