#Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira. 
#1ª string: AATTGGAA 2ª string: TG 3ª string: AAAA
string1 = input('Digite uma frase')
string2 = input('Digite uma frase')
string3 = ''
for letra in string1:
    if letra not in string2:
        string3 += letra
if string3 == '':
    print('Todos os caracteres foram removidos')
else:
    print(f'os caracteres das frases {string1} e {string2} foram removivod formando a string com os seguintes caracteres {string3 }')