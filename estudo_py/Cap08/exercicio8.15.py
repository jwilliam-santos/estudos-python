#Altere o Programa 7.2, o jogo da forca.
#Escolha a palavra a adivinhar utilizando números aleatorios.
#------------------------------------------------------------
#palavra = input("Digite a palavra secreta:").lower().strip()
#for x in range(100):
#    print()
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
#       else:
#            erros += 1
#            print("Você errou!")
#    print("X==:==\nX  :  ")
#    print("X  O  " if erros >= 1 else "X")
#    linha2 = ""
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
#progrma começa na proxíma linha (50)
import random
lista_palavras = ['xeon','Rx7600','Ram','linux','python']
palavra = random.randint(0,len(lista_palavras)  -1 )
digitadas = []
acertos = []
erros = 0
linhas_txt = """
X==:==
X  :
X
X
X
X
=======

"""

linhas = []

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

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
            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "\\"
            elif erros == 4:
                linhas[4][4] = "/"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"

    for l in linhas:
        print("".join(l))
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break