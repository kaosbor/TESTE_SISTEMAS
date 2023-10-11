'''
Exercício 3: Soma dos Números Pares
Descrição: Escreva um programa que calcula a soma dos números pares em uma lista fornecida pelo usuário.
Teste de Sistema: 

Cenário 1: Lista com Números Pares
Entrada: Lista: [2, 4, 6, 8, 10]
Saída Esperada: Resultado: A soma dos números pares é 30.

Cenário 2: Lista sem Números Pares
Entrada: Lista: [1, 3, 5, 7, 9]
Saída Esperada: Resultado: A lista não contém números pares.
'''

# Solicita ao usuário que insira a lista de números, separados por vírgulas e entre colchetes.
entrada = input("Digite uma lista de números (ex: [2, 4, 6, 8, 10]): ")

# Tenta converter a entrada em uma lista de números
try:
    lista = eval(entrada)
except NameError:
    lista = []

# Inicializa uma variável para a soma dos números pares
soma_pares = 0

# Percorre a lista e adiciona os números pares à soma
for numero in lista:
    if numero % 2 == 0:
        soma_pares += numero

# Verifica se a soma_pares é maior que zero para determinar se a lista contém números pares
if soma_pares > 0:
    print(f"Resultado: A soma dos números pares é {soma_pares}.")
else:
    print("Resultado: A lista não contém números pares.")

