#O que acontece se digitarmos 0,001 no programa anterior? 
# Caso ele não funcione, altere-o de forma a corrigir o problema
#Resposta: o programa não responde caso eu digite 0.001.
#proxima linha começa a correção do programa.
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
        if apagar < 0.0000000001: 
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
        elif atual == 0.01:
            atual = 0.0025
        elif atual == 0.0025:
            atual = 0.001
        cédulas = 0   
#Não e possivel arrumar o programa para aparecer o resultado. 
            