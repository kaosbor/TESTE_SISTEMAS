'''
Exercício 5: Média de uma Lista de Números
Descrição: Escreva um programa que calcula a média de uma lista de números fornecida pelo usuário.
Teste de Sistema:

Cenário 1: Lista com Números
Entrada: Lista: [5, 10, 15, 20]
Saída Esperada: Resultado: A média dos números é 12.5.

Cenário 2: Lista Vazia 
Entrada: Lista: []
Saída Esperada: Resultado: A lista está vazia, não é possível calcular a média.
'''

entrada = input("Digite uma lista de números (ex: [5, 10, 15, 20]): ") # Solicita ao usuário que insira a lista de números, separados por vírgulas e entre colchetes.
# Tenta converter a entrada em uma lista de números
try:
    lista = eval(entrada)
except NameError:
    lista = []
# Verifica se a lista está vazia
if not lista:
    print("Resultado: A lista está vazia, não é possível calcular a média.")
else:
    # Calcula a média dos números na lista
    media = sum(lista) / len(lista)
    print(f"Resultado: A média dos números é {media}.")