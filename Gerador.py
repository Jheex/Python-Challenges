import os

def criar_proximo_desafio():
    # 1. Listar todas as pastas no diretório atual
    pastas = [f for f in os.listdir('.') if os.path.isdir(f) and f.startswith('Desafio_')]
    
    numeros = []
    for p in pastas:
        try:
            # Extrai o número após o '_' (ex: de 'Desafio_05' pega '05')
            num = int(p.split('_')[1])
            numeros.append(num)
        except (IndexError, ValueError):
            continue

    # 2. Definir o próximo número da sequência
    proximo_num = max(numeros) + 1 if numeros else 1
    
    # 3. Formatar o nome da pasta com zero à esquerda (ex: Desafio_04)
    nome_pasta = f"Desafio_{proximo_num:02d}"
    
    # 4. Criar a pasta e o arquivo
    try:
        os.makedirs(nome_pasta)
        caminho_arquivo = os.path.join(nome_pasta, "desafio.py")
        
        # Cria o arquivo em branco
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"# {nome_pasta}\n") # Opcional: apenas um comentário inicial
            
        print(f"✅ Sucesso: '{nome_pasta}/desafio.py' criado!")
    except FileExistsError:
        print(f"⚠️ A pasta {nome_pasta} já existe.")

if __name__ == "__main__":
    criar_proximo_desafio()