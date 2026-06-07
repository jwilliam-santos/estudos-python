#Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado.
#Cada linha não deve conter mais de 76 caracteres.
#Cada página terá no máximo  60 linhas.
#Adiciona na última linha de cada página o número de página atual e o nome do arquivo original.
# obs: o arquivo "mobydick.txt" e o usado nesse exercicio
Largura = 76
linhasporpaginas = 60
pagatt = 1
linhas = 0
arquivo = open("mobydick.txt","r")
saida = open("saida.txt","w")
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