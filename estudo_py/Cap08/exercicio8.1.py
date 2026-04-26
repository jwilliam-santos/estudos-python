#Escreva uma função que retorne o maior de dois números.
#Valores esperados:
#máximo(5,6) == 6
#máximo(2,1) == 2
#máximo(7,7) == 7
def máx (a,b):
    if a > b:
        return a
    else:
        return b
print(f'máx (5,6) == {máx(5,6)}')
print(f'máx (7,7) == {máx(7,7)}')
print(f'máx (2,1) == {máx(2,1)}')