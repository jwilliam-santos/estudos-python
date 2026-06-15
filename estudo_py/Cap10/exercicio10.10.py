#Crie uma nova conta, agor a tendo João e José como clientese o saldo igual a 500
#Obs: Nesse exercicio foi usado a classe conta do arquivo contas2
from contas2 import Conta; from clientes import Cliente
joão = Cliente("João Silva","999")
josé = Cliente("José Pereira","1234")
conta = Conta([joão,josé],"1234",saldo=500)