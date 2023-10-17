'''
Exercício 11: Jogo da Forca
Descrição: Implemente o jogo da forca em que o computador escolhe uma palavra aleatória e o jogador tenta adivinhar as letras.
Teste de Sistema:

Cenário 1: Palavra Adivinhada Corretamente
Entrada:
Palavra escolhida pelo computador: "elefante"
Letras escolhidas pelo jogador: e, l, f, a, n, t
Saída Esperada: Resultado: Parabéns, você adivinhou a palavra!

Cenário 2: Tentativas Esgotadas
Entrada:
Palavra escolhida pelo computador: "banana"
Letras escolhidas pelo jogador: x, y, z, m, n, b
Saída Esperada: Resultado: Você esgotou suas tentativas. A palavra era "banana".
'''

import random

# Lista de palavras para o jogo
palavras = ["elefante", "banana", "computador", "python", "programacao", "jogo", "forca"]

# Escolhe uma palavra aleatória da lista
palavra = random.choice(palavras)

# Converte a palavra em minúsculas para facilitar a comparação
palavra = palavra.lower()

# Número máximo de tentativas
max_tentativas = 6

# Inicializa a lista de letras adivinhadas
letras_adivinhadas = ["_"] * len(palavra)

# Inicializa a lista de letras erradas
letras_erradas = []

# Inicializa o contador de tentativas
tentativas = 0

# Loop principal do jogo
while True:
    # Exibe a palavra oculta com as letras adivinhadas
    print("Palavra: " + " ".join(letras_adivinhadas))
    
    # Exibe as letras erradas
    if letras_erradas:
        print("Letras erradas: " + " ".join(letras_erradas))
    
    # Solicita ao jogador que adivinhe uma letra
    letra = input("Adivinhe uma letra: ").lower()
    
    # Verifica se a letra é válida (uma letra minúscula)
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, insira uma letra válida.")
        continue
    
    # Verifica se a letra já foi adivinhada
    if letra in letras_adivinhadas or letra in letras_erradas:
        print("Você já adivinhou essa letra.")
        continue
    
    # Verifica se a letra está na palavra
    if letra in palavra:
        # Atualiza a lista de letras adivinhadas
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        # A letra não está na palavra
        letras_erradas.append(letra)
        tentativas += 1

    # Verifica se o jogador ganhou
    if "_" not in letras_adivinhadas:
        print("Resultado: Parabéns, você adivinhou a palavra!")
        break

    # Verifica se o jogador esgotou suas tentativas
    if tentativas == max_tentativas:
        print(f"Resultado: Você esgotou suas tentativas. A palavra era '{palavra}'.")
        break