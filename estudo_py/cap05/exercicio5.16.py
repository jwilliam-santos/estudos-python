#execute o programa 5.1 para os seguntes valores:
#501, 745 384,2,7,1
#programa 5.1 na proxima linha, resultados após o programa.
valor = int(input('digitte o valor a pagar:'))
cédulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar  -= atual
        cédulas += 1
    else:
        print(f'{cédulas} cédulas(s) de R${atual}')
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0
# 1 cedula de 1 real em 501 e 10 cedulas de 50 reais
# em 745 foi 14 cedulas de 50 reais, 2 cedulas de 20 reais e uma cedula de 5 reais 
#em 384 foi 7 cedulas de 50 reais, uma cedula de 20 reais, uma cedula de 10 reais e 1 cedula de 5 reais
# em 2 foi 2 cedulas de 1 real
# em 7 foi 2 cedulas de 1 real e 1 cedula de 5 reais
# em 1 foi 1 cedula de 1 real