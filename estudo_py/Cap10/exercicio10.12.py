#Modifique as classes Conta e ContaEspecial para que a operação de saque retorne verdadeiro se o saque foi efetuado e falso, caso contrário.
class Cliente:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone
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
            return True
        if self.saldo < valor:
            print("Saldo insuficiente ao Sacar dinheiro ")
            return False
    def depósito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for operação in self.operações:
            print(f"{operação[0]:10s} {operação[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")
class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        super().__init__(clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return False
joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
phoenix = Cliente("Phoenix Da Silva","1234-1234")
conta1 = Conta([joão], número="001", saldo=1000)
conta2 = ContaEspecial([maria, joão], número="002", saldo=500, limite=1000)
conta3  = Conta([phoenix],número="003",saldo=100)
conta1.saque(50)
conta2.depósito(300)
conta1.saque(190)
conta2.depósito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
conta3.saque(50)
#Retornou True
conta3.saque(500)
#Retornou False