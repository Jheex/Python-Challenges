#1. usuario_correto = "admin"
#2. senha_correta = "1234"
#3. login = input("Digite seu login: ")
#4. senha = input("Digite sua senha: ")
#5. Se login for igual a usuario_correto E senha for igual a senha_correta:
#6. Imprima "Acesso Permitido"
#7. Senão: Imprima "Login ou Senha incorretos"

usuario_correto = "admin"
senha_correta = "1234"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == usuario_correto and senha == senha_correta:
    print("Acesso Permitido")
else:
    print("Login ou senha incorretos")



