#Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas. 
#1ª string: AAACTBF 2ª string: CBT Resultado: CBT A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
string1 = 'AAACTBF '
string2 = 'CBT'
stringcomum =''
for letra in string1:
    if letra in string2 and letra not in stringcomum:
        stringcomum += letra
if stringcomum == '':
    print('não ha caracter comum')
else:
    print(f'Existem {stringcomum} em comum')