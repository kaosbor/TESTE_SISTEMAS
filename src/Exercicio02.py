'''
Exercício 2: Contagem de Vogais
Descrição: Crie um programa que conta o número de vogais em uma frase fornecida pelo usuário.
Teste de Sistema:

Cenário 1: Frase com Vogais
Entrada: Frase: "Olá, mundo!"
Saída Esperada: Resultado: A frase possui 5 vogais.

Cenário 2: Frase sem Vogais
Entrada: Frase: "Nenhuma vogal aqui"
Saída Esperada: Resultado: A frase não possui vogais.
'''

# CÓDIGO LIMPO

def contar_vogais(frase):
    vogais = "AEIOUaeiou"
    count = 0
    for letra in frase:
        if letra in vogais:
            count += 1
    return count

frase = input("Digite uma frase: ")
numero_de_vogais = contar_vogais(frase)

if numero_de_vogais > 0:
    print(f"Resultado: A frase possui {numero_de_vogais} vogais.")
else:
    print("Resultado: A frase não possui vogais.")

# CÓDIGO COMENTADO

def contar_vogais(frase): # Definindo uma função (responsável por contar o número de vogais na frase fornecida) chamada contar_vogais que aceita uma frase como argumento. 
    vogais = "AEIOUaeiou" # Uma string que contém todas as vogais maiúsculas e minúsculas.
    count = 0 # Inicializa uma variável chamada "count" para contar o número de vogais na frase.
    for letra in frase: # Inicia um loop que percorre cada letra na frase.
        if letra in vogais: # Verifica se a letra atual está na lista de vogais.
            count += 1 # Se a letra for uma vogal, incrementa o contador "count" em 1.
    return count # Retorna o valor final do contador "count" como resultado da função.

frase = input("Digite uma frase: ") # Solicita ao usuário que insira uma frase e armazena-a na variável "frase".
numero_de_vogais = contar_vogais(frase) # Chama função "contar_vogais" que está acima, com a frase inserida pelo usuário e armazena o resultado em "numero_de_vogais".
if numero_de_vogais > 0: # Verifica se o número de vogais é > do que zero (ou seja, se há pelo menos uma vogal na frase).
    print(f"Resultado: A frase possui {numero_de_vogais} vogais.") # Se houver vogais, imprime quantas vogais foram encontradas.
else:
    print("Resultado: A frase não possui vogais.") # Se não houver vogais, imprime que NÃO há vogais.