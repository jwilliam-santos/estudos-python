#Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²)
#Valores esperados:
#área_quadrado(4) == 16
#área_quadrado(9) == 81
def área_quadrado(a):
    area = a*a
    return area
print(f'A área do quadrado é {área_quadrado(4)}')
print(f'A área do quadrado é {área_quadrado(9)}')