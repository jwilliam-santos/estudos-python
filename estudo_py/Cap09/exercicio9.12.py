#Modifique o programa do Exercício 9.11 para também registras a linha e a coluna de cada ocorrência da palavra no arquivo.
#Para isso, utilize lista nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.
#import sys
#nome = sys.argv[1]
#dic = {}
#arquivo = open (nome,"r")
#for linha in arquivo:
#    linha = linha.strip().lower()
#    palavra = linha.split()
#    for p in palavra:
#        if p in dic:
#            dic[p] +=1
#        else:
#            dic[p] = 1
#arquivo.close()
#print(dic)
#Programa começa na proxíma linha (18)
import sys
nome = sys.argv[1]
dic = {}
clinha = 1
coluna = 1
arquivo = open (nome,"r")
for linha in arquivo:
    linha = linha.strip().lower()
    palavra = linha.split()
    for p in palavra:
        if p == "":
            coluna += 1
            continue
        if p in  dic:
            dic[p].append((linha,coluna))
        else:
            dic[p] = (linha,coluna)
        coluna += len(p) + 1
    coluna += 1
    clinha += 1        
arquivo.close()
for c in dic:
    print(f"{c} = {dic[c]}")