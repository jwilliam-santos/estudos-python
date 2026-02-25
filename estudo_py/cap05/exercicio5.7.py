# modifique o programa anterior de forma q o usuario digite o inicio e o fim da tabuada em vez de começar de 1 a 10
#n = int(input(' Tabuada de:'))
#x = 2
#while  x <= 20:
#
#    x = x + 2
n = int(input(' Tabuada de :'))
inicio = int(input("De: "))
fim = int(input("Até: "))
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
