#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
#Pergunte também o valor mensal que será pago. 
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
divida = float(input('qual o vaolor inicial da sua divida'))
jurosmensal = float(input('qual o juros mensal da sua divida'))
valormensal = float(input('Qual o valor mensal que vc pagará sua divida?'))
mes = 1
if divida * (jurosmensal / 100)  > valormensal:
    print('Infelizmente sua divida nunca sera paga pois o juros e superior que o seu pagamento mensal ')
else:
    saldo = divida
    jurospago = 0
    while saldo  > valormensal:
        juros = saldo * (jurosmensal / 100)
        saldo = saldo + juros - valormensal
        jurospago = jurospago + juros
        print(f'no mes {mes} sua divida e de {saldo:2f}')
        mes = mes + 1
    print(f'Para pagar uma divida de {saldo:2f} a juros de %{jurospago}, mas vc presicara de {mes - 1} para pagar sua divida, no ultimo mes vc teria {saldo:2f} de saldo a pagar')