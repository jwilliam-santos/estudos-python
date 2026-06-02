#Modifique o programa do Exercício 9.1 para que receba mais dois parâmetros:
#a linha de início e a de fim pra impressão.
#O programa deve imprimir apenas as linha entre esses dois valores (incluido as linha de início e fim).
#------------------------------------------------------------------------------------------------------
#import sys
#nome_arquivo = sys.argv[1]
#arquivo =  open(nome_arquivo,'r')
#for linha in arquivo:
#    print(linha)
#arquivo.close()
#Programa começa na proxíma linha (12)
import sys
nome_arquivo = sys.argv[1]
y = int(sys.argv[2])
x = int(sys.argv[3])
arquivo =  open(nome_arquivo,'r')
contador = 1
for linha in arquivo:
    if contador >= y:
        print(linha)
    else:
        contador += 1
arquivo.close()