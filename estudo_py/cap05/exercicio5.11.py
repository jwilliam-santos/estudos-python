# Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança. 
# Exiba os valores de mês a mês para os 24 primeiros meses.
# Escreva o total de ganho com juros no período.
depositoinicial = float(input('Qual o valor da poupança'))
juros = float(input('Qual o valor de juros da poupança'))
mês = 1
total_juros = 0
while mês <= 24:
   rendimento = depositoinicial * (juros / 100)
   depositoinicial = depositoinicial + rendimento
   total_juros = total_juros + rendimento
   mês = mês + 1
print(f'Mês {mês}: R$ {depositoinicial:.2f}')
