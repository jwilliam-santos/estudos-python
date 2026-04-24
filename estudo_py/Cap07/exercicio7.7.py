#Escreva um programa que peça ao usuário que digite uma frase e imprima quantas vogais ela contém.
#Não considere maiúsculas e minúsculas como #diferentes. Exemplo: uma frase como “A casa” #deve
#imprimir três “as”.
frase = input('Digite uma frase ').lower()
vogais = ['a','e','i','o','u']
contador = ''
for letra in frase:
    if letra in vogais:
        contador += letra
print(f'a frase tem {contador} vogais')
    
    
