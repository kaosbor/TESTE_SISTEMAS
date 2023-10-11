'''
Exercício 7: Busca Binária
Descrição: Implemente um programa que realiza uma busca binária em uma lista ordenada de números inteiros.
Teste de Sistema:

Cenário 1: Número Encontrado
Entrada: Lista: [1, 3, 5, 7, 9, 11, 13, 15]
Buscar: 7
Saída Esperada: Resultado: O número 7 foi encontrado na posição 3.

Cenário 2: Número Não Encontrado
Entrada:
Lista: [2, 4, 6, 8, 10]
Buscar: 3
Saída Esperada: Resultado: O número 3 não foi encontrado na lista.
'''

def busca_binaria(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Solicita ao usuário que insira a lista ordenada de números
entrada_lista = input("Digite a lista ordenada de números (ex: 1, 3, 5, 7, 9, 11, 13, 15): ")

# Tenta converter a entrada em uma lista de números
try:
    lista = [int(x) for x in entrada_lista.split(',')]
except ValueError:
    lista = []

elemento = int(input("Digite o número a ser buscado: ")) # Solicita ao usuário que insira o número a ser buscado

posicao = busca_binaria(lista, elemento) # Realiza a busca binária

# Exibe o resultado
if posicao != -1:
    print(f"Resultado: O número {elemento} foi encontrado na posição {posicao}.")
else:
    print(f"Resultado: O número {elemento} não foi encontrado na lista.")