#Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira. 1ª string: AATTCGAA 2ª string: TG 3ª string: AC Resultado:AAAACCAA
string1 = input('Digite uma frase')
string2 = input('Digite uma frase')
string3 = input('Digite uma frase')
string4 = ''
if len(string2) != len(string3):
    print('Erro, A frase 2 e a frase 3 presisam ter o mesmo comprimento')
else:
    for letra in string1:
        if letra in string1  and  letra in string2:
            x = string2.find(letra)
            y = string3[x]
            string4 += y
        else:
            string4 += letra
print(f'A string final deu {string4}' )