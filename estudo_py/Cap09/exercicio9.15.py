#Altere o Programa 7.2, o jogo da forca. 
#Utilize um arquivo em que uma palavra seja gravada a cada linha.
#Use um editor de textos para gerar o arquivo.
#Ao iniciar o programa, utilize esse arquivo para carregar (ler) a lista de palavras.
#Experimente também perguntar o nome do jogador e gerar um arquivo com o número de acertos dos cinco melhores.
#-------------------------------------------------------------------------------------------------------------
#palavra = input("Digite a palavra secreta:").lower().strip()
#for x in range(100):
#   print()
#digitadas = []
#acertos = []
#erros = 0
#while True:
#    senha = ""
#    for letra in palavra:
#        senha += letra if letra in acertos else "."
#    print(senha)
#    if senha == palavra:
#        print("Você acertou!")
#        break
#    tentativa = input("\nDigite uma letra:").lower().strip()
#    if tentativa in digitadas:
#        print("Você já tentou esta letra!")
#        continue
#    else:
#        digitadas += tentativa
#        if tentativa in palavra:
#            acertos += tentativa
#        else:
#            erros += 1
#            print("Você errou!")
#    print("X==:==\nX  :  ")
#    print("X  O  " if erros >= 1 else "X")
#   linha2 = ""
#    if erros == 2:
#        linha2 = "  |  "
#    elif erros == 3:
#        linha2 = " \|  "
#    elif erros >= 4:
#        linha2 = " \|/ "
#    print(f"X{linha2}")
#    linha3 = ""
#    if erros == 5:
#        linha3 += " /   "
#    elif erros >= 6:
#        linha3 += " / \ "
#    print(f"X{linha3}")
#    print("X\n===========")
#    if erros == 6:
#        print("Enforcado!")
#        break
#Programa começa na proxíma linha (53)
import random
import sys
arquivo = open("palavras.txt", "r")
lista_de_palavras = arquivo.readlines()
arquivo.close()
palavra = random.choice(lista_de_palavras).lower().strip()

digitadas = []
acertos = []
erros = 0
while True:
    
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break