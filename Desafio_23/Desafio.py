# --- ÁREA DAS FUNÇÕES (Onde você cria as "máquinas") ---

# 1. Crie uma função chamada 'metros_para_centimetros':
    # Ela deve pedir um valor em metros (float)
    # Calcular: centimetros = metros * 100
    # Exibir o resultado formatado

# 2. Crie uma função chamada 'celsius_para_fahrenheit':
    # Ela deve pedir a temperatura em Celsius (float)
    # Calcular: fahrenheit = (celsius * 9/5) + 32
    # Exibir o resultado formatado


# 3. Crie uma função chamada 'quilos_para_gramas':
    # Ela deve pedir o peso em quilos (float)
    # Calcular: gramas = quilos * 1000
    # Exibir o resultado formatado


# --- CORPO PRINCIPAL (Onde o programa roda) ---

# 4. Inicie o loop 'while True'

    # 5. Exiba o Menu de Conversão:
    # 1 - Metros para Centímetros
    # 2 - Celsius para Fahrenheit
    # 3 - Quilos para Gramas
    # 4 - Sair

    # 6. Receba a opção do usuário (input)

    # 7. Use IF / ELIF para chamar a função correta:
        # Se opção for 1: metros_para_centimetros()
        # Se opção for 2: celsius_para_fahrenheit()
        # Se opção for 3: quilos_para_gramas()
    
    # 8. Opção 4 para Sair (break)

def metros_para_centimetros():
    print("teste")
    metros = float(input("Digite um valor em metros: "))
    centimetros = metros * 100
    print("O valor em centímetros é: ",centimetros)

def celsius_para_fahrenheit():
    celsius = float(input("Digite um valor em celcius: "))
    fahrenheit = celsius * 9/5 + 32
    print("O valor em fahrenheit é: ",fahrenheit)

def quilos_para_gramas():
    quilos = float(input("Digite um valor em quilos: "))
    gramas = quilos * 1000
    print("O valor em gramas é: ",gramas)

while True:
    print("-----MENU-----")
    print("1 - Metros para Centímetros")
    print("2 - Celsius para Fahrenheit")
    print("3 - Quilos para Gramas")
    print("4 - Sair")
    opcao = int(input("Selecione uma opção: "))
    print("")

    if opcao == 1:
        metros_para_centimetros()
    elif opcao == 2:
        celsius_para_fahrenheit()
    elif opcao == 3:
        quilos_para_gramas()
    elif opcao == 4:
        print("Saindo....")
        break
    else:
        print("Opção inválida!")
    


