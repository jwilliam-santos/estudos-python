#Modifique o programa do Exercício 9.7 para também receber o número de caracteres pos linha e número de linhas por página pela linha de comando.
#Largura = 76
#linhasporpaginas = 60
#pagatt = 1
#linhas = 0
#arquivo = open("mobydick.txt","r")
#saida = open("saida.txt","w")
#for linha in arquivo:
#    linha_tratada = linha.rstrip("\n")[:Largura]
#    saida.write( linha_tratada + "\n")
#    linhas += 1
#    if linha == (linhasporpaginas -1):
#        saida.write(f"[Arquivo: mobydick.txt | Página: {pagatt}]\n")
#    pagatt += 1
#    linhas = 0
#arquivo.close()
#saida.close()
import sys
Largura = int(sys.argv[1])
linhasporpaginas = int(sys.argv[2])
pagatt = 1
linhas = 0
arquivo = open("mobydick.txt","r")
saida = open("saida2.txt","w")
for linha in arquivo:
    linha_tratada = linha.rstrip("\n")[:Largura]
    saida.write( linha_tratada + "\n")
    linhas += 1
    if linha == (linhasporpaginas -1):
        saida.write(f"[Arquivo: mobydick.txt | Página: {pagatt}]\n")
    pagatt += 1
    linhas = 0
arquivo.close()
saida.close()