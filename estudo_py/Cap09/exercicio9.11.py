#Crie um programa que leia um arquivo e crie um dicionário em que cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.
import sys
nome = sys.argv[1]
dic = {}
arquivo = open (nome,"r")
for linha in arquivo:
    linha = linha.strip().lower()
    palavra = linha.split()
    for p in palavra:
        if p in dic:
            dic[p] +=1
        else:
            dic[p] = 1
arquivo.close()
print(dic)