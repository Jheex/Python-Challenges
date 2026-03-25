# Desafio_47

import json

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    email = input("Digite seu e-mail: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    with open ("Desafio_47/cadastro.json", "r") as arquivo:
        dados = json.load(arquivo)

    dados.append(usuario)

    with open ("Desafio_47/cadastro.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Arquivo JSON\n", dados)