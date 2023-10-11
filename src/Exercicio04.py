'''
Exercício 4: Contagem de Palavras em uma Frase
Descrição: Crie um programa que conta o número de palavras em uma frase fornecida pelo usuário.
Teste de Sistema:

Cenário 1: Frase com Palavras
Entrada: Frase: "O rato roeu a roupa do rei de Roma"
Saída Esperada: Resultado: A frase possui 8 palavras.

Cenário 2: Frase sem Palavras
Entrada: Frase: colocar nada, deixra vazio 
Saída Esperada: Resultado: A frase não possui palavras.
'''

# CÓDIGO LIMPO

frase = input("Digite uma frase: ") # Solicita ao usuário que insira a frase
frase = frase.strip() # Remove espaços em branco extras no início e no final da frase
if not frase: # Verifica se a frase está vazia
    print("Resultado: A frase não possui palavras.")
else:
    # Divide a frase em palavras usando espaços em branco como delimitadores
    palavras = frase.split()
    numero_de_palavras = len(palavras)
    print(f"Resultado: A frase possui {numero_de_palavras} palavras.")