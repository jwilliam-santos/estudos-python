#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo
#segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
#podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
# + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
num1 = int(input(' Digite um numero'))
num = int(input('Digite o segundo numero'))
n = 1
x = 0
while n <= num:
    x = x + num1
    n = n +1
print(f' {num1} x {num} = {x}')
