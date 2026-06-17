#Altere a classe ContaEspecial de forma que seu extrato exiba o limite e o total disponível para saque.
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
     
    def mostrar(self): 
        print(f"Extrato CC N° {self.número}\n")
        self.total = self.saldo + self.limite
        for operação in self.operações:
            print(f"{operação[0]:10s} {operação[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:7.2f}\n Limite: {self.limite:10.2f}\n Disponível para o Saque {self.total:10.2f} \n")
        

joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
phoenix = Cliente("Phoenix Da Silva","1234-1234")
kant = Cliente("Emmanuel Kant","9876-1234")
conta1 = Conta([joão], número="001", saldo=1000)
conta2 = ContaEspecial([maria, joão], número="002", saldo=500, limite=1000)
conta3  = Conta([phoenix],número="003",saldo=100)
conta4 = ContaEspecial([kant], número="12", saldo=500, limite=1000)
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
#EX10.13 A SEGUIR
conta4.mostrar()