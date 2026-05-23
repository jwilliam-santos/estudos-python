#Modifique o jogo do alienígena.
#Crie uma variável que represente a vida do jogador com 100.
#A partida termina quando você encontrar o alienígena ou quando a vida acabar (<=0).
#A cada derro, diminua a vida por um valor aleatório entre 5 e 20, representando um ataque do alienígena.
#Você pode retirar parte do jogo que limita o número de tentavias e deixar apenas a vida do jogador ou do alienígena decidirem quando a partida termina.
#Exiba a vida do jogador antes de perguntar a próxima.
#--------------------------------------------------------------------------------------------------------------------------------------
#import random
#
#MAX_TENTATIVAS = 3
#árvore = random.randint(1, 100)
#print("Um alienígena está escondido atrás de uma árvore")
#print("Cada árvore foi numerada de 1 a 100.")
#print("Você tem 3 tentativas para adivinhar em que árvore")
#print("o alienígena se esconde.")
#
#for tentativa in range(1, MAX_TENTATIVAS + 1):
#    palpite = int(input(f"Árvore {tentativa}/{MAX_TENTATIVAS }: "))
#    if palpite == árvore:
#        print(f"Você acertou na {tentativa}\u00aa tentativa")
#        break
#    elif palpite > árvore:
#        print("Muito alto")
#    else:
#        print("Muito baixo")
#else:
#    print("Você não conseguiu acertar.")
#    print(f"O alienígena estava na árvore {árvore}")
# Programa começa na proxíma linha (30)
import random
vida = 100
árvore = random.randint(1, 100)

print("Um alienígena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print("o alienígena se esconde.")
print('Sua vida e 100')
while True:
    palpite = int(input('Digite seu palpite'))
    
    ataque_alien = random.randint(5,20)
    
    if palpite == árvore:
        print(f"Você acertou")
        break   
    elif palpite > árvore:
           print("Muito alto")
           dano_alien = vida - ataque_alien
           print(f'Sua vida atual está {dano_alien}')
    else:
        print("Muito baixo")
        dano_alien = vida - ataque_alien
        print(f'Sua vida atual está {dano_alien}')
    if vida <= 0:
        print('Você perdeu')
        break
