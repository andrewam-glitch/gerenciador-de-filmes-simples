# Gerenciador simples de filmes 🎬

# 1. Pega os títulos separados por vírgula
filmes = input("Digite os títulos dos filmes separados por vírgula: ").split(',')

# Remove espaços extras
filmes = [f.strip() for f in filmes]

# 2. Mostra informações iniciais
print(f"\nTotal de filmes cadastrados: {len(filmes)}")
print(f"Primeiro filme da lista: {filmes[0]}")
print(f"Último filme da lista: {filmes[-1]}")

# 3. Adiciona um novo filme no final da lista
novo_final = input("\nDigite um filme para adicionar ao final da lista: ")
filmes.append(novo_final)

# 4. Adiciona um filme no início da lista
novo_inicio = input("Digite um filme para adicionar no início da lista: ")
filmes.insert(0, novo_inicio)

# 5. Remove um filme pelo nome
remover = input("Digite o nome de um filme para remover: ")
if remover in filmes:
    filmes.remove(remover)
else:
    print("Esse filme não está na lista!")

# 6. Mostra a lista em ordem alfabética
print("\nFilmes em ordem alfabética:")
for f in sorted(filmes):
    print("-", f)

# 7. Inverte a lista e mostra
filmes.reverse()
print("\nLista invertida:")
for f in filmes:
    print("-", f)

# 8. Faz uma cópia da lista
copia_filmes = filmes.copy()
filmes.clear()

# 9. Mostra as duas listas
print("\nLista original (agora vazia):", filmes)
print("Cópia dos filmes:", copia_filmes)
