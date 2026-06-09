#Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas. 
#O arquivo de saída também não deve ter mais de uma linha em branco repetida.
import sys
arquivo_de_entrada = sys.argv[1]
arquivoent = open(arquivo_de_entrada,"r")
arquivosai = open("pt2ex9.14.txt","w")
branco = 0
for linha in arquivoent:
        linha.rstrip()
        linha = linha.replace(" ","")
        if linha == "":
                branco += 1
        else:
            branco  = 0
        if branco < 2:
               arquivosai.write(linha + "\n")
arquivoent.close()
arquivosai.close()