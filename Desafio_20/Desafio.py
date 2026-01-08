#O Desafio: O Oráculo Numérico
#    Definição: Crie uma variável numero_secreto e atribua um valor fixo a ela (ex: 42).
#    Tentativas: O programa deve perguntar o palpite do usuário.
#    Dicas lógicas:
#        Se o palpite for menor que o secreto: "Muito baixo! Tente um maior."
#        Se o palpite for maior que o secreto: "Muito alto! Tente um menor."
#    O Contador: Toda vez que o usuário errar, você deve somar +1 em uma variável tentativas.
#    Finalização: Quando ele acertar, dê os parabéns e mostre em quantas chances ele conseguiu.
#    Tratamento: Não deixe o programa travar se ele digitar letras.
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("")
print("Seja bem vindo ao Oraculo númerico!")
while True:
    try:
        print("Digite um número e o sistema apontará se está perto ou não!")
        print("Atenção!! Você tem 10 tentativas!")
        print("Tentativa: ",tentativas)
        resposta = (int(input("Digite um número: ")))
        tentativas += 1
        
    except ValueError:
            print("Digite somente números!")
            continue
    if resposta == numero_secreto:
        print("")
        print("Parabéns! Você acertou!")
        print(f"Você acertou em {tentativas}")
        print("")
        break
    elif resposta < numero_secreto:
        print("")
        print("Muito baixo! Tente um maior")
        print("")
    elif resposta > numero_secreto:
        print("")
        print("Muito Alto! Tente um menor")
        print("")
    elif tentativas >= 10:
         print("Você atingiu o limite de tentativas!")
         print(f"A resposta era {numero_secreto}")
         break