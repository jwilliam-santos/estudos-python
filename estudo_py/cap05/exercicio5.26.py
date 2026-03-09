#escreva um programa que calcule o resto de uma divisão inteira entra 2 números.
#Utilize apenas operações de soma e subtração para calcular o resto.
divisor = int(input('Digite o divisor da sua conta'))
dividendo = int(input('Digite o dividendo da sua conta'))
quociente = 0
x =dividendo 
while x >= divisor:
    x -= divisor
    quociente += 1
resto = x
print('o resto da sua conta deu {}'.format(resto))
