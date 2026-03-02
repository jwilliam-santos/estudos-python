#escreva um programa que leia numeros inteiro do teclado.
#O programa deve ler os numeros até que o usuario digite 0 (zero).
#No final da execução exiba a quantidade de numeros digitados,
#  assim como a soma e a media aritimetica
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite numeros para somar ou digite 0 (zero) para sair '))
    if numero == 0:
        print('tchau')
        break
    soma = soma + numero
    quantidade = quantidade + 1
print('vc digitou {} numeros'.format(quantidade))
print(f'a soma dos numeros que vc digitou deu {soma}')
print(f'a media aritimetica dos numeros que vc digitou deu {soma / quantidade}')
