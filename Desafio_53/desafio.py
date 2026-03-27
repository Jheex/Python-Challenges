"""
Peça uma senha e verifique:

Se tiver menos de 8 caracteres → "Senha fraca"
Caso contrário → "Senha válida"
"""

senha = input("Digite sua senha: ")

quantidade = len(senha)

if quantidade < 8:
    print("Senha fraca")
else:
    print("Senha válida")