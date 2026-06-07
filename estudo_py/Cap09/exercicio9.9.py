#Crie um programa que receba uma lista de nomes de arquivos e os imprima, um por um
import sys
arquivo1 = sys.argv[1:]
for nomearquivo in arquivo1:
    arquivo = open(nomearquivo,"r")
    print(arquivo.read())
    arquivo.close()