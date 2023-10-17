'''
Exercício 12: Simulador de Banco
Descrição: Crie um programa que simule as operações de um banco, como depósito, saque e verificação de saldo.
Teste de Sistema:

Cenário 1: Depósito e Saque Bem Sucedidos
Entrada:
Saldo inicial: R$ 500
Depósito: R$ 200
Saque: R$ 100
Saída Esperada: Resultado: Saldo atual: R$ 600

Cenário 2: Tentativa de Saque com Saldo Insuficiente
Entrada:
Saldo inicial: R$ 100
Saque: R$ 200
Saída Esperada: Resultado: Saldo insuficiente para realizar o saque.
'''

print("Cenário 1: Depósito e Saque Bem Sucedidos")

class Banco:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def verificar_saldo(self):
        return self.saldo

# Solicita o saldo inicial do usuário
saldo_inicial = float(input("Saldo inicial: R$ "))
banco = Banco(saldo_inicial)

# Solicita o valor do depósito do usuário
valor_deposito = float(input("Depósito: R$ "))
if banco.deposito(valor_deposito):
    print("Depósito bem-sucedido.")
else:
    print("Depósito mal-sucedido.")

# Solicita o valor do saque do usuário
valor_saque = float(input("Saque: R$ "))
if banco.saque(valor_saque):
    print("Saque bem-sucedido.")
else:
    print("Saque mal-sucedido.")

# Verifica o saldo atual
saldo_atual = banco.verificar_saldo()
print(f"Saldo atual: R$ {saldo_atual}")

print("\nCenário 2: Tentativa de Saque com Saldo Insuficiente")

class Banco:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def verificar_saldo(self):
        return self.saldo

# Solicita o saldo inicial do usuário
saldo_inicial = float(input("Saldo inicial: R$ "))
banco = Banco(saldo_inicial)

# Solicita o valor do saque do usuário
valor_saque = float(input("Saque: R$ "))
if banco.saque(valor_saque):
    print("Saque bem-sucedido.")
else:
    print("Resultado: Saldo insuficiente para realizar o saque.")

# Verifica o saldo atual
saldo_atual = banco.verificar_saldo()
print(f"Saldo atual: R$ {saldo_atual}")