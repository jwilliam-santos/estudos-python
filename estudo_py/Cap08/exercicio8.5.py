#Reescreva a função do Programa 8.1 de forma a utilizar os metodos de pesquisa  em lista, vistor no Cap07.
#---------------------------------------------------------------------------------------------------------------
#def pesquise(lista, valor):
#    for x, e in enumerate(lista):
#        if e == valor:
#           return x
#    return None
#L = [10, 20, 25, 30]
#print(pesquise(L, 25))
#print(pesquise(L, 27))
#programa começa na proxima linha (12)
L = [10,20,25,30]
def pesquise(L,x) :
    L = [10,20,25,30]
    if x in L:
       p =  L.index(x)
       return p
    else:
        print('Número não foi encontrado na lista')
print(pesquise(L, 25))
print(pesquise(L, 27))

    

