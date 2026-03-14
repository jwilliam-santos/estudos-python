#faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
lista1 = []
lista2 = []
while True:
    x = int(input('Digite um numero para a primeira lista ( o numero 0 sai)'))
    lista1.append(x)
    if x == 0:
        break
while True:
    y = int(input('Digite um numero para a segunda lista ( o numero 0 sai)'))
    lista1.append(y)
    if  y == 0:
        break
lista3 = lista1[:]
lista3.extend(lista2)
x = 0
while x < len(lista3):
    x += 1
print(f'{x}: {lista3}')
