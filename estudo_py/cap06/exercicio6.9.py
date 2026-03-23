#Modifique o exemplo para pesquisar dois valores.
#Em vez de apenas p,leia outro valor v que também será procurado.
#Na impressão, indique qual dos dois valores foi achado primeiro.
#---------------------------------------------------------------
#Programa 6.9
#L = [15,7,27,39]
#p = int(input('Digite o valor a procurar:'))
#achou = False
#x = 0
#while x < len(L):
#   if L[x] == p:
#       achou = True
#       break
#   x +=1
#if achou:
#   print(f'{p} achado na posição {x}')
#else:
#   print(f'{p} não encontrado ')
#Exercicio 6.9 começa na proxima linha (20)
L = [15,7,27,39]
p = int(input('Digite o valor a procurar:'))
v = int(input('Digite o valor a procurar:'))
achoup = False
achouv = True
n =0
x = 0
while x < len(L):
   if L[x] == p:
      achoup = True
      if not achouv:
         n = 1
   x +=1
   if L[x] == v:
      achouv = True
      if not achoup:
         n = 2
   x += 1
if achoup:
    print(f"p: {p} encontrado")
else:
    print(f"p: {p} não encontrado")
if achouv:
    print(f"v: {v} encontrado")
else:
    print(f"v: {v} não encontrado")
if n == 1:
    print("p foi achado antes de v")
elif n == 2:
    print("v foi achado antes de p")

       