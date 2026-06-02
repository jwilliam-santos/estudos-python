#Crie um programa que leia os arquivos pares.txt e ímpares.txt e crie um só arquivo pareseimpares com todas as linha dos outros 2 arquivos , de forma a preservar a ordem númerica.
#with open("ímpares.txt", "w") as ímpares:
#    with open("pares.txt", "w") as pares:
#        for n in range(0, 1000):
#            if n % 2 == 0:
#                pares.write(f"{n}\n")
#            else:
#                ímpares.write(f"{n}\n")
#OBS: esse programa acima foi usado para criar os arquivos ímpares.txt e pares.txt
import sys
par =  open('pares.txt','r') 
impar = open('ímpares.txt','r')
tudo_junto = open('tudojunto.txt','w')
lista_pares = par.readlines()
lista_impares = impar.readlines()
for i in range(len(lista_pares)):
    tudo_junto.write(lista_pares[i])

    tudo_junto.write(lista_impares[i])
par.close()
impar.close()
tudo_junto.close()