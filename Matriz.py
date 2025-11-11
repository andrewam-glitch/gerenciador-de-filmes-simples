matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

#Lembrando que começa por zero (n-1)
idx_linha = 1
idx_coluna = 2
print(matriz[idx_linha][idx_coluna])
print(matriz[2])
print(matriz)

##print('\n----------------------')

for linha in matriz:
    for coluna in linha:
        print(valor, end=' ')
print()




#1. Escreva um programa em Python que leia os valores de uma matriz 3x3
#fornecidos pelo usuário. O programa deve solicitar, um a um, os elementos de
#cada posição da matriz, armazena-los em uma lista de listas e, ao final, exibir
#a matriz completa na tela formatado de linhas e colunas

matriz = []
num_linhas = int(input(f"Digite a quantidade de linhas: "))
num_colunas = int(input(f"Digite a quantidade de colunas: "))

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        valor = int(input(f"Digite o valor da posição [{i}[{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    for valor in linha:
        print(valor, end=' ')
    print()