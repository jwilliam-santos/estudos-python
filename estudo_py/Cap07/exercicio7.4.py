#Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC Resultado: T: 2x A: 2x C: 1x
string = input('Digite uma frase')
contador = {}
for letra in string:
    if letra in contador:
        contador[letra] = contador[letra] + 1
    else:
        contador[letra] = 1
print(contador)

