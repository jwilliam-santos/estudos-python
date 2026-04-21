#Escreva um programa que leia duas strings.
#Verifique se a segunda ocorre dentro da primeira e imprima posição de início. 
#1ª string: AABBEFAATT 2ª string: BE Resultado: BE encontrado na posição 3 de AABBEFAATT
string1 = 'AABBEFAAT'
string2 = 'BE'
if string2 in string1:
    print('A segunda string (BE) foi encontrada na posição 3 da primeira string')
