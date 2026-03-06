#Modifique o programa  para aceitar valors decimais, ou seja, támbem contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50
#while True:
#    if atual <= apagar:
#        apagar  -= atual
#        cédulas += 1
#    else:
#        print(f'{cédulas} cédulas(s) de R${atual}')
#        if apagar == 0:
#           break
#        if atual == 50:
#            atual = 20
#        elif atual == 20:
#            atual = 10
#        elif atual == 10:
#            atual = 5
#        elif atual == 5:
#            atual = 1
#        cédulas = 0
#programa começa na proxima linha
valor = float(input('digite o valor a pagar:'))
cédulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        apagar = round(apagar, 2)  
        cédulas += 1
    else:
        if cédulas > 0:
            print(f'{cédulas} cédula(s) de R${atual}')
        if apagar < 0.01: 
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual == 0.25
        elif atual == 0.25:
            atual == 0.10
        elif atual == 0.10:
            atual == 0.05
        elif atual == 0.05:
            atual == 0.01
        cédulas = 0
        
