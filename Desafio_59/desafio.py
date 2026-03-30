# Desafio_59

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def falar(self):
        print(f"Meu nome é {self.nome} e sou um {self.especie}")

a1 = Animal("Branquelo", "gato")
a2 = Animal("PO", "panda")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Jhonatan", 20)
p2 = Pessoa("Ana", 23)

print(a1.nome)
print(a2.nome)
print(p1.nome)
print(p2.nome)
a1.falar()
a2.falar()

