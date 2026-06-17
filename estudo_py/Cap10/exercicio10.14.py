#Observe o método saque das classes Conta e ContaEspecial.
#Modifique o método saque da classe Conta de forma que a verificação da possibilidade de saque seja feita por um novo método, substituindo a condição atual.
#Esse novo método retornará verdadeiro se o saque puder ser efetuado, e falso, caso contrário. 
#Modifique a classe ContaEspecial de forma a trabalhar com esse novo método. 
#Verifique se você ainda precisa trocar o método saque de ContaEspecial,
#ou apenas o novo método criado para verificara possibilidade de saque.
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
    def pode_sacar(self,valor):
        if self.saldo >= valor:
            return True
        else:
            return False
    def saque(self, valor):# Tirar o "valor real" e retornar True or False se puder ou não
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
    
    def pode_sacar(self,valor):
        if self.saldo + self.limite >= valor:
            return True
        else:
            return False
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return False
     
    def mostrar(self): # On This Def: Exibir Limite Para o Saque, e o Total Disponivel Pro saque
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
#EX10.14 A seguir
python = Cliente("python da silva","5555-1111")
python = Conta([python], número="32", saldo=1000)
Java = Cliente("Java Pereira","1111-5555")
Java = ContaEspecial([Java], número="54", saldo=1000,limite = 200) 

Java.pode_sacar(1400) #Com o Terminal Interativo Resultado: False
python.pode_sacar(1001)#Com o Terminal Interativo Resultado: False
