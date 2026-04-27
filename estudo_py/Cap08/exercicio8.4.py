#Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A= (base x altura) /2 )
#Valores esperador:
#área_triângulo(6,9) == 27
#área_triângulo(5,8) == 20
def área_triângulo(a,b):
    area = (a*b) /2
    return area
print(f'A area do triângulo deu {área_triângulo(6,9)}')
print(f'A area do triângulo deu {área_triângulo(5,8)}')