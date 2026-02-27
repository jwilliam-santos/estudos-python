#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim
#como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.
#lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes
#que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco
#vezes de 20.
dividendo = int(input('Digite  o numero dividendo'))
divisor= int(input('Digite o numero divisor'))
x = dividendo
quociente = 0
while  x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f'Sua conta deu {quociente} de quociente e {resto} de resto   ')



