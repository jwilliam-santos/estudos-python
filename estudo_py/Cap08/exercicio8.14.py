#Altere o Programa 8.22 de forma que o usuário tenha três chances de acertar o número.
#O programa termina se o usuário acertar ou errar três vezes.
#-------------------------------------------------------------------------------------
#import random
#n = random.randint(1, 10)
#x = int(input("Escolha um número entre 1 e 10:"))
#if x == n:
#    print("Você acertou!")
#else:
#    print("Você errou.")
#Programa começa na proxíma linha (12)
import random
tentativas = 0
n =  random.randint(1, 10)
while True:
    x = int(input("Escolha um número entre 1 e 10:"))
    if x == n:
        print("Você acertou!")
        tentativas += 1
    else:
        print('Você errou.')
        tentativas += 1
    if tentativas == 3:
        print('Jogo acabou.')
        break