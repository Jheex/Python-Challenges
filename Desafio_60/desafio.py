# Desafio_60

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

p1 = Pessoa("Jhonatan", 20)
p2 = Pessoa("João", 29)
p1.apresentar()
p2.apresentar()