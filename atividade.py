# BLOCO 1 — Incrementadores e Decrementadores

# 1. Contagem simples
x = 0
for i in range(5):
    x += 1
print(f"Valor final de x: {x}\n")

# 2. Contagem regressiva
num = int(input("Digite um número para contagem regressiva: "))
while num >= 0:
    print(num)
    num -= 1
print("Fim da contagem!\n")

# 3. Dobro acumulado
valor = 1
while valor <= 100:
    print(valor)
    valor *= 2
print("Finalizado!\n")

# 4. Incremento misto
a = 3
b = 7
while a <= b:
    a += 2
    b -= 1
print(f"Valor final de a: {a}, b: {b}\n")

# 5. Saldo bancário
saldo = 0
for i in range(3):
    deposito = float(input(f"Digite o valor do depósito {i+1}: "))
    saldo += deposito
print(f"Saldo final: R${saldo:.2f}\n")


# BLOCO 2 — Estruturas de Repetição (for e while)

# 1. Tabuada
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print()

# 2. Soma de 1 a N
n = int(input("Digite um número para somar de 1 até N: "))
soma = 0
i = 1
while i <= n:
    soma += i
    i += 1
print(f"Soma total: {soma}\n")

# 3. Números pares
print("Números pares de 1 a 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print()

# 4. Leitura de notas
soma_notas = 0
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma_notas += nota
media = soma_notas / 5
print(f"Média das notas: {media:.2f}\n")

# 5. Contagem até parada
cont = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    cont += 1
print(f"Você digitou {cont} números.\n")


# BLOCO 3 — Contadores e Acumuladores

# 1. Contar positivos
positivos = 0
for i in range(10):
    num = float(input(f"Digite o número {i+1}: "))
    if num > 0:
        positivos += 1
print(f"Total de números positivos: {positivos}\n")

# 2. Soma condicional
soma_maiores = 0
for i in range(5):
    num = float(input(f"Digite o número {i+1}: "))
    if num > 10:
        soma_maiores += num
print(f"Soma dos números maiores que 10: {soma_maiores}\n")

# 3. Média ponderada
soma_pesos = 0
soma_ponderada = 0
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    peso = float(input(f"Digite o peso da nota {i+1}: "))
    soma_pesos += peso
    soma_ponderada += nota * peso
media_ponderada = soma_ponderada / soma_pesos
print(f"Média ponderada: {media_ponderada:.2f}\n")

# 4. Soma até limite
total = 0
while total < 100:
    num = float(input("Digite um número: "))
    total += num
print(f"Total final: {total}\n")

# 5. Maior valor
maior = None
for i in range(5):
    num = float(input(f"Digite o número {i+1}: "))
    if maior is None or num > maior:
        maior = num
print(f"O maior número digitado foi: {maior}\n")

# BLOCO 4 — Controle de Fluxo (break e continue)

# 1. Busca de número
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    if num == 99:
        print("Número encontrado!")
        break
print()

# 2. Pular negativos
print("Digite 7 números:")
for i in range(7):
    num = float(input(f"Número {i+1}: "))
    if num < 0:
        continue
    print(f"Número positivo: {num}")
print()

# 3. Senha de acesso
while True:
    senha = input("Digite a senha: ")
    if senha == "python123":
        print("Acesso permitido!\n")
        break
    else:
        print("Senha incorreta, tente novamente.")

# 4. Contagem de tentativas
import random
secreto = random.randint(1, 10)
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    tentativas += 1
    if palpite == secreto:
        print(f"Acertou! Tentativas: {tentativas}\n")
        break
    else:
        print("Errou! Tente novamente.")

# 5. Menu interativo
while True:
    print("MENU:")
    print("1 - Mostrar mensagem")
    print("2 - Somar dois números")
    print("3 - Encerrar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá, bem-vindo ao menu!\n")
    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Soma: {n1 + n2}\n")
    elif opcao == "3":
        print("Encerrando...\n")
        break
    else:
        print("Opção inválida!\n")

# BLOCO 5 — Desafio Final

# 1. Simulador de pontuação
pontos = 0
rodadas = 0
while True:
    valor = int(input("Digite a pontuação da rodada (número negativo para parar): "))
    if valor < 0:
        break
    pontos += valor
    rodadas += 1
print(f"Rodadas jogadas: {rodadas}, Pontuação total: {pontos}\n")

# 2. Caixa de supermercado
total = 0
produtos = 0
while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))
    if preco == 0:
        break
    total += preco
    produtos += 1
print(f"Total da compra: R${total:.2f}, Quantidade de produtos: {produtos}\n")

# 3. Jogo de adivinhação
import random
segredo = random.randint(1, 20)
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número (1 a 20): "))
    tentativas += 1
    if palpite == segredo:
        print(f"Acertou! Tentativas: {tentativas}\n")
        break
    elif palpite < segredo:
        print("O número é MAIOR!")
    else:
        print("O número é MENOR!")

# 4. Controle de estoque
estoque = int(input("Digite o estoque inicial do produto: "))
vendas = 0
while estoque > 0:
    venda = int(input("Digite a quantidade vendida: "))
    if venda <= estoque:
        estoque -= venda
        vendas += 1
        print(f"Venda registrada. Estoque restante: {estoque}")
    else:
        print("Quantidade inválida!")
print(f"Estoque zerado. Total de vendas: {vendas}\n")

# 5. Gerador de sequência
n = int(input("Digite o número de termos da sequência: "))
soma = 0
for i in range(1, n + 1):
    soma += i
    print(soma)
print("Fim da sequência!")
