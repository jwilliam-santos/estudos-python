#Modifique o programa 6.13 de forma a perguntar o número de salas disponíveis no cinema, assim como a quantidade de lugares em cada uma delas.
#---------------------------------------------------------------------------------------------------------------------------------------------
##Programa 6.13
#lugares_vagos = [10, 2, 1, 3, 0]
#while True:
#    sala = int(input("Sala (0 sai): "))
#    if sala == 0:
#        print("Fim")
#        break
#    if sala > len(lugares_vagos) or sala < 1:                          
#        print("Sala inválida")
#    elif lugares_vagos[sala - 1] == 0:
#        print("Desculpe, sala lotada!")
#    else:
#        lugares = int(
#            input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")
#        )
#        if lugares > lugares_vagos[sala - 1]:
#            print("Esse número de lugares não está disponível.")
#        elif lugares < 0:
#            print("Número inválido")
#        else:
#            lugares_vagos[sala - 1] -= lugares
#            print(f"{lugares} lugares vendidos")
#print("Utilização das salas")
#for sala, vagos in enumerate(lugares_vagos):
#    print(f"Sala {sala + 1} – {vagos} lugar(es) vazio(s)")
#programa começa na proxima linha (29)
número_de_salas = int(input('Existem quantas salas?'))
lugares_vagos = []
for sala in range(número_de_salas):
    lugares_vagos.append(int(input(f'Há quantos lugares vagos na sala { sala + 1}')))
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(
            input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")
        )
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} – {vagos} lugar(es) vazio(s)")
print('Vendas:')
total_de_ingressos_vendidos = 0
for sala, vendas in enumerate:
    print(f'Sala {sala + 1} - {total_de_ingressos_vendidos} vendido(s)')
    total_de_ingressos_vendidos += vendas
print(f"Total de ingressos vendidos: {total_de_ingressos_vendidos}")