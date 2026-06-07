#Crie um programa que receba uma lista de nomes de arquivo e que gere apenas um grande arquivo de saída.
import sys
arquivos = sys.argv[1:]
arquivoctd = open("pt2ex9.10.txt","w")
for linha in arquivos:
    arquivoctd.write(linha)
arquivoctd.close()
