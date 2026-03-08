#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
# Imprima a tabuada da operação escolhida. 
# Repita até que a opção saída seja escolhida.
while True:
    menu = (input('Digite as opçoes, adição[+]. subtração[-], divisão[/] ou multiplicação[X] ou 0 (zero) para sair'))
    if menu == 0:
        print('Tchau')
        break
    n = int(input('qual o número da Tabuada que vc deseja ver'))
    x = 1
    while x <= 10:
        if menu == ' +':
            print(f' {n} + {x} = { n + x}')
        elif menu == ' -':
            print(f' {n} - {x} = {n - x}')
        elif menu == ' X':
            print(f' {n} x {x} = {n * x}')
        elif menu == ' /':
            print(f' {n} / {x} = { n / x}')
        x += 1
    else:
        print('Operação Invalida')