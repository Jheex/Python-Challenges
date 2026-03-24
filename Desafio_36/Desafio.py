
score = 0

tamanho_tv = float(input("Qual o tamanho da TV: "))
watts = float(input("Qual o consumo de energia em watts: "))
valor = float(input("Qual o valor em R$: "))
hdmi = int(input("Qual o número de portas HDMI: "))

if tamanho_tv > 80:
    score = score + 4
elif tamanho_tv > 60 and tamanho_tv < 81:
    score = score + 3
else:
    score = score - 1

if watts < 200:
    score = score + 1 

if valor < 1000:
    score = score + 3

elif valor >= 1000 and valor < 2001:
    score = score + 2

elif valor >= 2000 and valor < 5001:
    score = score + 1


if hdmi > 6:
    score = score + 3
elif hdmi >= 4 and hdmi < 7:
    score = score + 2

if score < 0:
    print("Score: 0")
elif score > 10:
    print("Score: 10")
else:
    print(score)