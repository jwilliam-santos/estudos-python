#Altere o Programa 7.2, o jogo da forca.
#Dessa vez, utilize as funções de tempo para cronometrar a partida.
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
#   else:
#        digitadas += tentativa
#        if tentativa in palavra:
#            acertos += tentativa
#        else:
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
#   elif erros >= 6:
#        linha3 += " / \ "
#    print(f"X{linha3}")
#    print("X\n===========")
#    if erros == 6:
#        print("Enforcado!")
#        break
#Programa começa na proxíma linha (49)
import time
palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
tm1 = time.perf_counter()

while True:
    tm2 = time.perf_counter()
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
tm2 = time.perf_counter()
tf = tm2 - tm1
print(f"O tempo de sua partida foi {tf}")