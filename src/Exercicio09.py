'''
Exercício 9: Calculadora de Fatorial
Descrição: Escreva um programa que calcula o fatorial de um número fornecido pelo usuário.
Teste de Sistema: 

Cenário 1: Fatorial de 5
Entrada: Calcular o fatorial de 5
Saída Esperada: Resultado: O fatorial de 5 é 120.

Cenário 2: Fatorial de 0
Entrada: Calcular o fatorial de 0
Saída Esperada: Resultado: O fatorial de 0 é 1.
'''

# Solicita ao usuário que insira o número para o qual deseja calcular o fatorial
numero = int(input("Calcular o fatorial de: "))

# Verifica se o número é negativo
if numero < 0:
    print("Resultado: O fatorial de um número negativo não é definido.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"Resultado: O fatorial de {numero} é {fatorial}.")