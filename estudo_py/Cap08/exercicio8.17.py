#Melhore o programa do exercício anterior perguntando ao jogador ao  nível de dificuldade desejado.
#No modo fácil, a vida começa com 100 e o alienígena pode causar entre 5 e 20 de dano, como anteriomente.
#No modo médio a vida começa com 80 e o alienígena pode causar danos entre 10 e 25.
#Já no modo difícil, a vida começa com 75 e o alienígena causa danos entre 20 e 30. 
#Adicione mensagens e caracteres para deixar o jogo mais divertido. :D
#---------------------------------------------------------------------------------------------------------
#import random
#vida = 100
#árvore = random.randint(1, 100)
#
#print("Um alienígena está escondido atrás de uma árvore")
#print("Cada árvore foi numerada de 1 a 100.")
#print("o alienígena se esconde.")
#print('Sua vida e 100')
#while True:
#    palpite = int(input('Digite seu palpite'))
#    
#    ataque_alien = random.randint(5,20)
#    
#    if palpite == árvore:
#        print(f"Você acertou")
#        break   
#    elif palpite > árvore:
#           print("Muito alto")
#           dano_alien = vida - ataque_alien
#           print(f'Sua vida atual está {dano_alien}')
#    else:
#        print("Muito baixo")
#        dano_alien = vida - ataque_alien
#        print(f'Sua vida atual está {dano_alien}')
#    if vida <= 0:
#        print('Você perdeu')
#        break
# O programa começa na linha (35)
import random
árvore = random.randint(1, 100)
while True:
    escolha = int(input('Digite o modo entre o fácil (1),médio (2) ou difícil (3)'))
    if escolha == 1:
        vida = 100
        break
    elif escolha == 2:
        vida = 80
        break   
    elif escolha == 3:
        vida = 75
        break
    else:
        print('Opção invalida digite 1, 2 ou 3')

árvore = random.randint(1, 100)
print("Um alienígena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print("o alienígena se esconde.")
print(f'Sua vida e {vida}')
while True:
    palpite = int(input('Digite seu palpite'))
    
    ataque_alien = random.randint(5,20)
    
    if palpite == árvore:
        print(f"Você acertou")
        break   
    elif palpite > árvore:
           print("Muito alto")
           vida = vida - ataque_alien
           print(f'Sua vida atual está {vida}')
    else:
        print("Muito baixo")
        vida = vida - ataque_alien
        print(f'Sua vida atual está {vida}')
    if vida <= 0:
        print('Você perdeu')
        break