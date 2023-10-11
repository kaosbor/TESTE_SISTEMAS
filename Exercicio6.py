'''
Exercício 6: Verificação de Palíndromo
Descrição: Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente).
Teste de Sistema:

Cenário 1: Palavra Palíndroma
Entrada: Palavra: "radar"
Saída Esperada: Resultado: A palavra "radar" é um palíndromo.

Cenário 2: Palavra Não Palíndroma
Entrada: Palavra: "hello"
Saída Esperada: Resultado: A palavra "hello" não é um palíndromo.
'''
palavra = input("Digite uma palavra: ") # Solicita ao usuário que insira uma palavra
palavra = palavra.strip() # Remove espaços em branco extras no início e no final da palavra
palavra_invertida = palavra[::-1] # Inverte a palavra
# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"Resultado: A palavra \"{palavra}\" é um palíndromo.")
else:
    print(f"Resultado: A palavra \"{palavra}\" não é um palíndromo.")