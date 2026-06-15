#Classe conta a ser alterada no exercicio 10.9
class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.depósito(saldo)

    def resumo(self):
        print(f"CC N°{self.número} Saldo: {self.saldo:10.2f}")
        for c in  self.clientes:
            print(f"Um Cliente é {c.nome} e o Seu telefone é {c.telefone}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        if self.saldo < valor:
            print("Saldo insuficiente ao Sacar dinheiro ")

    def depósito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for operação in self.operações:
            print(f"{operação[0]:10s} {operação[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")