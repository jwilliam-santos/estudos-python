#Crie um programa que imprima as linhas de um arquivo.
#Esse programa deve receber três parâmetros pela linha de comando:
#o nome do arquivo, a linha inicial e a última linha a imprimir
import  sys
nome_arquivo = sys.argv[1]
linha_inicial = int(sys.argv[2])
ultima_linha = int(sys.argv[3])
arquivo = open (nome_arquivo,"r")
for c in arquivo.readlines()[linha_inicial -1: ultima_linha]:
    print(c[:-1])
arquivo.close()