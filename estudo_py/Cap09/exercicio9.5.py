#Crie um programa que inverta a ordem das linhas do arquivo 'pares.txt' A primeira linha deve contaer o maior número e a última o menor.
import sys

pares = open('paresex9.5pt2.txt','r')
saída = open('pt3ex9.5.txt','w')
L = pares.readlines()
L.reverse()
for l in L:
    saída.write(l)

pares.close()
saída.close()
