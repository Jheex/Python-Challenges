# Desafio_46
import json

while True:
    nome = input("Qual seu nome? ")
    idade = int(input("Qual a sua idade? "))

    cadastro = {
        "nome": nome,
        "idade": idade
    }

    with open ("Desafio_46/usuarios.json", "r") as arquivo:
        dados = json.load(arquivo)

    dados.append(cadastro)

    with open("Desafio_46/usuarios.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Item adicionado com sucesso\n",dados)

