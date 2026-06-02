#Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo.
import sys
nome_arquivo = sys.argv[1]
arquivo =  open(nome_arquivo,'r')
for linha in arquivo:
    print(linha)
arquivo.close()