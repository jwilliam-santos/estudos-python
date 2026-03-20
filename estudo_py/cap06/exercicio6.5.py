#Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
#Atualmente, apenas um comando pode ser inserido por vez.
#Altere-o de forma a considerar operação como uma string.
#---------------------------------------------------------------------------------------------
#Exemplo: FFFAAAS siginificaria três chegadas de novos clientes,Três atendimentos e , finalmente a saída do Programa.
#Programa 6.7 de exemplo:
# último = 10
# fila = list(range(1,último + 1 ))
#while True:
#   print(f"\n\Existem {len(fila)} clientes na fila ")
#   print(f" Fila atual: {fila}" )
#   print(" Digite F para adicionar um cliente ao fim da fila, ")
#   print("ou A para realizar o atendimento. S para sair.")
#   operação = input("Operação (F,A ou S)")
#   if operção == "A":
#       if len(fila) > 0
#       atendido = fila.pop(0)
#       print(f"Cliente {atendido} atendido")
#       else:
#           print("Fila Vazia Ninguém para atender")
#   elif operação == "F"
#       último += 1 #incrementa o ticket do novo cliente
#   elif operação == "S":
#           break
#   else:
#       print("Operação inválida! Digite apenas F,A ou S!")
#programa começa na proxima linha (28)
último = 10
fila = list(range(1,último + 1 ))
while True:
   print(f"\n\Existem {len(fila)} clientes na fila ")
   print(f" Fila atual: {fila}" )
   print(" Digite F para adicionar um cliente ao fim da fila, ")
   print("ou A para realizar o atendimento. S para sair.")
   operação = input("Operação (F,A ou S)")
   x = 0
   sair = False
   while  x < len(operação):
    if operação[x] == 'A':
        atendido = fila.pop(0)
        print(f"Cliente {atendido} atendido")
    elif operação[x] == 'F':
       último += 1
       print(f'cliente {último} foi atendido')
    elif operação[x] == 'S':
        sair = True
        break
    else:
       print('Digite apenas F,A ou S')
    x += 1
    if sair:
       break
