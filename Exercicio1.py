'''
Exercício 1: Verificação de Número Primo
Descrição: Escreva um programa que verifica se um número fornecido pelo usuário é primo ou não.
Teste de Sistema:

Cenário 1: Número Primo
Entrada: Número: 17
Saída Esperada: Resultado: O número 17 é primo.

Cenário 2: Número Não Primo
Entrada: Número: 10
Saída Esperada: Resultado: O número 10 não é primo.
'''

# CÓDIGO LIMPO

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Digite um número inteiro positivo: "))
    if is_prime(num):
        print(f"Resultado: O número {num} É primo.")
    else:
        print(f"Resultado: O número {num} NÃO é primo.")
except ValueError:
    print("[ERRO] Por favor, insira um número inteiro válido.")

# CÓDIGO COMENTADO

# Função para verificar se um número é primo
def is_prime(number): # Esta linha define uma função chamada is_prime que recebe um número como argumento.
    if number <= 1: # Verifica se o número é menor ou igual a 1.
        return False # Se for, a função retorna False (F), pois números menores ou iguais a 1 não são primos.
    if number <= 3: # Esta condição verifica se o número é menor ou igual a 3.
        return True #  Se for, a função retorna True (V), pois os números 2 e 3 são primos.
    if number % 2 == 0 or number % 3 == 0: # Verifica se o número é divisível por 2 ou por 3 (ou seja, se o resto da divisão por 2 ou por 3 é igual a zero).
        return False # Se qualquer uma dessas condições for verdadeira, a função retorna False, pois isso indica que o número não é primo.
    i = 5 # Uma variável i é inicializada com o valor 5. Esta variável será usada em um loop para verificar se o número é divisível por outros números maiores do que 3.
    while i * i <= number: # Este loop continuará enquanto o valor de i multiplicado por ele mesmo for < ou = ao número que estamos verificando. Isso é feito para otimizar o processo de verificação de primos.
        if number % i == 0 or number % (i + 2) == 0: # Dentro do loop, este verifica se o número é divisível por i ou "i + 2". A verificação começa com i = 5 e i + 2 = 7, e depois se move para valores subsequentes de i e "i + 2".
            return False # Se o número for divisível por qualquer um deles, a função retorna False (F), indicando que o número não é primo.
        i += 6 # Após cada iteração do loop, i é incrementado em 6. Isso é feito para verificar se o número é divisível por números que não são múltiplos de 2 ou 3, economizando assim verificações desnecessárias.
    return True # Se o loop terminar sem encontrar nenhum divisor para o número, a função retorna True (V), indicando que o número é primo.

# Solicitar entrada do usuário
try: # Estrutura de controle "bloco try-except", para definir um bloco de código onde exceções (erros) podem ocorre
    num = int(input("Digite um número inteiro positivo: ")) # O programa tenta obter um número inteiro positivo da entrada do usuário e o armazena na variável num.
    if is_prime(num): # Verifica se o número num é primo usando a função is_prime que foi definida anteriormente.
        print(f"Resultado: O número {num} É primo.") # Se for primo, esta imprime indicando que o número É primo.
    else: # Se o número não for primo, o código entra no bloco else.
        print(f"Resultado: O número {num} NÃO é primo.") # Imprime uma mensagem indicando que o número NÃO é primo.
except ValueError: # Este bloco except lida com exceções do tipo ValueError, que podem ocorrer se o usuário inserir algo que não possa ser convertido em um número inteiro válido.
    print("[ERRO] Por favor, insira um número inteiro válido.") # Se uma exceção ValueError for lançada (por exemplo, se o usuário inserir texto em vez de um número), esta linha imprimirá uma mensagem de erro solicitando que o usuário insira um número inteiro válido.