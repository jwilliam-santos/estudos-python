#Escreva um programa que leia um número e verifique se é ou não um número primo.
#Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
#Se o resto de uma dessas divisões for igual a zero, o número não é primo.
#Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
#codigo na proxíma linha (6)
n = int(input('Digite um número inteiro'))
if n == 2 :
    print(f'O número é primo pois e {n}')
elif n < 0:
    print('Número invalido digite numero positivo')
elif  n == 1 or n == 0:
    print(f'o numero e primo porque o numero {n} e um caso especial')
elif  n % 2 == 0:
    print('o numero não e primo pós ele e par')
else: 
    x = 3
    while x < n:
        if n % x == 0:          
            break
        x += 2
        if x == n:
            print('o número {} e primo'.format(n))    
        else:
            print(f'o numero {n} não e primo pois  e divisivel por {x}')
    