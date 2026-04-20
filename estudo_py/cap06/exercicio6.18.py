#Modifique o Programa 6.20 para ordenar a lista em ordem descrescente.
#L = [1,2,3,4,5] deve ser ordenada como L = [5,2,3,2,1].
#---------------------------------------------------------------------
##Programa 6.20
#L = [7, 4, 3, 12, 8]
#fim = 5
#while fim > 1:
#    trocou = False
#    x = 0
#    while x < (fim - 1):
#        if L[x] > L[x + 1]:
#           trocou = True
#            temp = L[x]
#            L[x] = L[x + 1]
#            L[x + 1] = temp
#       x += 1
#    if not trocou:
#        break
#    fim -= 1
#for e in L:
#    print(e)
#Programa começa na proxíma linha (23)
L = [1,2,3,4 ,5 ]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou: 
        break
    fim -= 1
for e in L:
    print(e)
