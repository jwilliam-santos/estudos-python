#Escreva um generator capaz de gerar uma sequência com o fatorial de 1 até, em que n é passacomo como parâmetro para o gerador. 
def fatorial(n):
    x = 1
    for xa in range(x,n+1):
        x *= xa
        yield x
for resultado in fatorial(5):
    print(resultado)
    