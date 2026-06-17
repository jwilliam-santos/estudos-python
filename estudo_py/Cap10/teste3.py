from clientes import Cliente
from contas3 import Conta, ContaEspecial

joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
conta1 = Conta([joão], número="001", saldo=1000)
conta2 = ContaEspecial([maria, joão], número="002", saldo=500, limite=1000)
conta1.saque(50)
conta2.depósito(300)
conta1.saque(190)
conta2.depósito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()