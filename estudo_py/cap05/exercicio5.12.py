#altere o programa anterios de forma a perguntas tambem o valor do depositado mensalmente. esse valor será depositado no inicio de cada mes.
#vc deve consideralo  para o calculo de juros
#depositoinicial = float(input('Qual o valor da poupança'))
#juros = float(input('Qual o valor de juros da poupança'))
#mês = 1
#total_juros = 0
#while mês <= 24:
#   rendimento = depositoinicial * (juros / 100)
#   depositoinicial = depositoinicial + rendimento
#   total_juros = total_juros + rendimento
#   mês = mês + 1
#print(f'Mês {mês}: R$ {depositoinicial:.2f}')
#inicio codigo na linha 14( proxima linha)
depositoinicial = float(input('Qual o valor da poupança'))
juros = float(input('Qual o valor de juros da poupança'))
valor_mensal = float(input('Qual o valor que você ira depositar'))
mês = 1
saldo = depositoinicial
total_juros = 0
while mês <= 24:
   saldo = saldo + (saldo + (juros / 100)) + valor_mensal
   print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
   mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depositoinicial:8.2f}.")

