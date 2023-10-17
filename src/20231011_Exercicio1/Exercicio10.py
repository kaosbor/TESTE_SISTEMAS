'''
Exercício 10: Validador de Senha
Descrição: Crie um programa que verifica se uma senha atende aos seguintes critérios:
Pelo menos 8 caracteres de comprimento.
Contém pelo menos uma letra maiúscula e uma letra minúscula.
Contém pelo menos um caractere especial.
Pelo menos um número.

Teste de Sistema:

Cenário 1: Senha Válida
Entrada: Senha: Abcdefg1
Saída Esperada: Resultado: A senha é válida.

Cenário 2: Senha Inválida (Falta de Número)
Entrada: Senha: Abcdefgh
Saída Esperada: Resultado: A senha deve conter pelo menos um número.
'''

import re

# Solicita ao usuário que insira a senha
senha = input("Digite a senha: ")

# Verifica o comprimento da senha
if len(senha) < 8:
    print("Resultado: A senha deve ter pelo menos 8 caracteres.")
else:
    # Verifica se a senha contém pelo menos uma letra maiúscula e uma letra minúscula
    if not (any(c.islower() for c in senha) and any(c.isupper() for c in senha)):
        print("Resultado: A senha deve conter pelo menos uma letra maiúscula e uma letra minúscula.")
    # Verifica se a senha contém pelo menos um caractere especial
    elif not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\]', senha):
        print("Resultado: A senha deve conter pelo menos um caractere especial.")
    # Verifica se a senha contém pelo menos um número
    elif not any(c.isdigit() for c in senha):
        print("Resultado: A senha deve conter pelo menos um número.")
    else:
        print("Resultado: A senha é válida.")