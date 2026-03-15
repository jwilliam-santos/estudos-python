#faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
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
lista3 = list(set(lista1 + lista2))
print(f'a sua lista total sem numeros repitidos deu {lista3}')