#Reescreva o Programa 8.2 de forma a utilizar for em vez do while.
#-----------------------------------------------------------------
#def soma(L):
#    total = 0
#    x = 0
#        total += L[x]
#        x += 1
#    return total
#
#
#L = [1, 7, 2, 9, 15]
#print(soma(L))
#print(soma([7, 9, 12, 3, 100, 20, 4]))
#Programa começa na proxima linha (15)
def soma(L):
    total = 0
    x = 0
    for x in L:
        total += x
    return total


L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))

