#Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem
#em uma delas. 1ª string: CTA 2ª string: ABC 3ª string: BT A ordem dos caracteres da terceira string não é importante.
string1 = input('Digite uma frase')
string2 = input('Digite uma frase')
string3 = ''
for letra in string1:
    if letra not in  string2 and letra not in string3:
        string3 += letra
for letra in string2:
    if letra not in string1 and letra not in string3:
        string3 += letra
if string3 == '':
    print('não há cacactere incommun')
else:
    print(f'os cacarcteres incommuns são {string3}')
