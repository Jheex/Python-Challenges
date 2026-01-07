# --- DESAFIO DA LISTA DE CONVIDADOS ---

# 1. Crie a lista inicial com "Ana", "Beto" e "Caio"
#convidados = ["Ana", "Beto", "Caio"]
#print(f"Lista inicial: {convidados}")

# 2. ADICIONAR: A "Duda" chegou!
# Dica: Use o .append() para colocar ela no final
#convidados.____("Duda") 
#print(f"Após adicionar Duda: {convidados}")

# 3. EDITAR: O "Beto" agora é "Roberto"
# Dica: O Beto está na posição [1]. Use convidados[1] = "Roberto"
#convidados[__] = "Roberto"
#print(f"Após editar o nome do Beto: {convidados}")

# 4. EXCLUIR: O "Caio" não vem mais
# Dica: Use o .remove("Nome") para tirar ele da lista
#convidados.____("Caio")
#print(f"Após o Caio sair: {convidados}")

# 5. EXIBIR: Mostre como ficou o churrasco
#print(f"Lista final do churrasco: {convidados}")

#Aprendendo a adicionar, editar e excluir!

convidados = ["Ana", "Beto", "Caio"]

print(f"Lista inicial: {convidados}")

convidados.append("Duda") #adicionando!

convidados[1] = "Roberto" #editando
print(f"Após editar o nome do Beto: {convidados}")

convidados.remove("Caio")#removendo
print(f"Após o caio sair: {convidados}")

print(f"Lista final do churrasco: {convidados}")
