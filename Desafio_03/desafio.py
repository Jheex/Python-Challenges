#1. Crie uma lista chamada 'candidatos' com os nomes: "Ana", "Jhonatan", "Marcos"
#2. Inicie um laço 'for' para percorrer cada 'nome' na lista 'candidatos'
#3. Crie um 'if' que verifica se o 'nome' é igual a "Jhonatan" (use == e aspas)
#4. Se for verdade, imprima: "Candidato Jhonatan encontrado!"
#5. Crie um 'else' para os outros casos
#6. Imprima: "Candidato " + nome + " em espera."

candidatos = ["Ana", "Jhonatan", "Marcos"]

for i in candidatos:
    if i == "Jhonatan":
        print("Candidato Jhonatan encontrado!")
    else:
        print("Candidato", i, "em espera")