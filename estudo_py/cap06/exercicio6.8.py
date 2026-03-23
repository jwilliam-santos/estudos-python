#Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou.
#Dica:observe a condição de saída do while
#-------------------------------------------------------------------------------------------------------------------
#Programa 6.9:
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
#Exercicio 6.8 começa na proxima linha (19)
L = [15,7,27,39]
p = int(input('Digite o valor a procurar:'))
achou = False
x = 0
while x < len(L):
   if L[x] == p:
       achou = True
       break
   x +=1
if achou:
   print(f'{p} achado na posição {x}')
else:
   print('Não foi achado')