# --- ÁREA DA FUNÇÃO (A Máquina) ---

# 1. Crie a função 'converter_para_mm' que recebe o parâmetro (metros)
    # 2. Use o RETURN para devolver o cálculo: metros * 1000

# --- CORPO PRINCIPAL (O Mundo Real) ---

# 3. Peça ao usuário um valor em metros (use float(input(...)))
# Guarde na variável: valor_digitado

# 4. A HORA DA CONEXÃO:
# Crie a variável 'resultado_mm'
# Ela deve receber a função 'converter_para_mm' passando o 'valor_digitado' dentro dela.


# 5. Dê um print na variável 'resultado_mm'

def converter_para_mm(metros):
    converter = metros * 1000
    return converter

while True:
    valor_digitado = float(input("Insira um valor em metros: "))
    resultado_mm = converter_para_mm(valor_digitado)
    print("Valor convertido em Milimetros",resultado_mm)