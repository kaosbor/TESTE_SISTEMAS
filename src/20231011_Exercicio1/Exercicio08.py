'''
Exercício 8: Ordenação de Lista
Descrição: Crie um programa que ordena uma lista de números inteiros em ordem crescente.
Teste de Sistema:

Cenário 1: Lista Desordenada
Entrada: Lista: [9, 2, 5, 1, 7, 3]
Saída Esperada: Resultado: Lista ordenada: [1, 2, 3, 5, 7, 9]

Cenário 2: Lista Já Ordenada
Entrada: Lista: [1, 2, 3, 4, 5]
Saída Esperada: Resultado: Lista já está ordenada: [1, 2, 3, 4, 5]
'''

# Solicita ao usuário que insira a lista de números
entrada_lista = input("Digite a lista de números (ex: 9, 2, 5, 1, 7, 3): ")

# Tenta converter a entrada em uma lista de números
try:
    lista = [int(x) for x in entrada_lista.split(',')]
except ValueError:
    lista = []

# Verifica se a lista está vazia
if not lista:
    print("Resultado: A lista está vazia.")
else:
    # Ordena a lista em ordem crescente
    lista_ordenada = sorted(lista)

    # Verifica se a lista já está ordenada
    if lista == lista_ordenada:
        print(f"Resultado: Lista já está ordenada: {lista}")
    else:
        print(f"Resultado: Lista ordenada: {lista_ordenada}")