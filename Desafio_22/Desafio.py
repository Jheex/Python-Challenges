n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

print("Selecione a opção desejada: ")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
resposta = int(input("Escreva o numero: "))

if resposta == 1:
  print("Somando")
  soma = n1 + n2
  print(f"Resultado: {soma}")
  if soma % 2 == 0:
    print(f"O numero é par")
  else:
    print("O numero é impar")
  if soma >= 0:
    print("O numero é positivo")
  else:
    print("O numero é negativo")
  if soma % 1 == 0:
    print("Inteiro")
  else:
    print("Decimal")
elif resposta == 2:
  print("Somando")
  sub = n1 - n2
  print(f"Resultado: {sub}")
  if sub % 2 == 0:
    print(f"O numero é par")
  else:
    print("O numero é impar")
  if sub >= 0:
    print("O numero é positivo")
  else:
    print("O numero é negativo")
  if sub % 1 == 0:
    print("Inteiro")
  else:
    print("Decimal")
elif resposta == 3:
  print("Multplicando")
  mult = n1 * n2
  print(f"Resultado: {mult}")
  if mult % 2 == 0:
    print(f"O numero é par")
  else:
    print("O numero é impar")
  if mult >= 0:
    print("O numero é positivo")
  else:
    print("O numero é negativo")
  if mult % 1 == 0:
    print("Inteiro")
  else:
    print("Decimal")
elif resposta == 4:
  print("Dividindo")
  div = n1 / n2
  print(f"Resultado: {div}")
  if div % 2 == 0:
    print(f"O numero é par")
  else:
    print("O numero é impar")
  if div >= 0:
    print("O numero é positivo")
  else:
    print("O numero é negativo")
  if div % 1 == 0:
    print("Inteiro")
  else:
    print("Decimal")
else:
  print("Valor invalido")
