from clientes import Cliente
from banco import Banco
from contas2 import Conta
joão = Cliente("João da Silva","3241-5599")
maria = Cliente("Maria Silva","7231-9955")
josé = Cliente("José Vargas","1234")
contaJM = Conta([joão,maria],100)
contaJ = Conta([josé],10)
tatu = Banco("Tatu")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
contaJM.depósito(1000)
contaJ.depósito(500)
contaJM.saque(40.54)
tatu.lista_contas()