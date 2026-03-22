#Modifique o programa para trabalhar com duas filas.
#  Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. 
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.
# --------------------------------------------------------------------------------------------------------------------
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
#Programa começa na proxima linha (27)
fila1 = []
fila2 = []
ultimo  = 10 
while True:
    print(f' Existem {len(fila1)} clientes na fila e  {len(fila2)} na fila 2 ')
    print(f'Fila 1 atual:{fila1}')
    print(f'Fila 2 atual: {fila2}')
    print('Comandos para a fila 1: A para atendimento e F para adicionar clientes (Que chegam ao fim da fila)')
    print('Comandos para a fila 2: B para atendimento e G para adicionar clientes (Que chegam ao fim da fila)')
    print('S para sair (serve nas 2 filas)')
    operação = input('Operação (A,F;S;B,G)')
    x = 0 
    sair  = False
    while x < len(operação):
        if operação[x] == 'A' or operação[x] == 'F':
            fila = fila1
        else:
            fila = fila2
        if operação[x] == "A" or operação[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F" or operação[x] == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(
                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
            )
        x = x + 1
    if sair:
        break