# Desafio_57
'''
🎯 Quer um exercício para treinar?
EXERCÍCIO:

Peça ao usuário para digitar um número.
Seu programa deve:

Tentar converter para número
Se falhar, mostrar “Erro: digite apenas números!”
Continuar pedindo até o usuário acertar
Quando digitar certo, mostrar “Número válido!” e parar
'''
while True:
    try:
        print("")
        numero = int(input("Digite um número: "))
        print(f"Funcionou, resposta: {numero}")
    except:
        print("Resposta inválida")