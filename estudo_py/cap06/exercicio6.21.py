#Escreva um programa que compare duas listas.
#Utilizando operações com conjuntos, imprima:
# os valores comuns ás duas listas
# os valoes que só existem na primeira 
# os valores que existem apenas na segunda
# uma lista com os elementos não repetidos das duas listas
# a primeira lista sem os elementos repetidos nas segunda
lista1 = [1, 2, 6, 8]
lista2 = [3, 6, 8, 9]
conjunto1 = lista1
conjunto2 = lista2
print(f'Lista 1 = {lista1} ')
print(f'Lista 2 = {lista2}')
print(f'valores em comum nas 2 listas {conjunto1 & conjunto2}')
print(f'valores que so tem na primeira lista {conjunto1 - conjunto2}')
print(f'valores que so tem na segunda lista {conjunto2 - conjunto1}')
print(f'valores não repetidos nas 2 listas {conjunto1 ^conjunto2}')
print(f'valores da primeira lista não repetidos na segunda lista {conjunto1 - conjunto2}')