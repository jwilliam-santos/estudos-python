#Modifique o Programa 6.6 usando for.
#Explique por que nem todos os while podem ser tranformados em for
#-----------------------------------------------------------------
#Programa 6.6
#L = []
#while True:
#    n = int(input("Digite um número (0 sai):"))
#    if n == 0:
#        break
#    L.append(n)
#x = 0
#while x < len(L):
#    print(L[x])
#    x += 1
#exercicio começa na proxima linha (15)
# O primeiro while não pôde ser convertido em for porque
# o número de repetições é desconhecido no início.