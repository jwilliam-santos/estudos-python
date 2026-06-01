#Escreva uma função que gere os números como a função range do Python.
#Essa função recebe três parâmetros de seu comportamento muda se passarmos um,dos ou três parâmetros.
#Chame-a de faixa.
#Exemplos:
# list(faixa(1))
# [0,1]
# list(faixa(1,10))
# [1,2,3,4,5,6,7,8,9,10]
#list(faixa(0,10,2))
# [0,2,4,6,8,10]
#VocÊ deve ter percebido que, diferente do range, a função faixa considera o fim do intervalo fechado, ou seja o último número que faz parte da faixa.
def faixa(x,b=None,passo =1 ):
    if b == None:
        inicio = 0
        fim = x
        
    if b!= None:
        inicio = x
        fim = b
    for c in range(1,fim+1,passo):
        yield c
print(list(faixa(5)))
print(list(faixa(1, 10)))
print(list(faixa(0, 10, 2)))