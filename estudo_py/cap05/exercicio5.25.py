#escreva um programa que calculea raiz quadrada de um número .
#Utilize o metodo de Newton para obter um resultado aproximado.
#Sendo n o número para obter a raiz quadrada, considere a base b=2.
#Calcule p usando a formula p = (b+(n/b)) / 2.
# Agora calcule o quadrado de p.
#A cada passo faça b = p e recalcule p usando a formula aprensentada
# Pare quando a diferenç entre n e o quadrado de p for menor que 0,0001.
n = int(input('Digite um número para obter a raiz quadrada dele'))
b = 2
x = (n - ( b* b))
while abs(n- (b*b)) > 0.0001:
    p = (b+(n/b))/2
    b = p
print(f'A raiz quadrada de {n} deu {p:8.4f}')
