#Crie um programa que receba o nome de dois arquivos.
#Como parâmetros da linha de comando e que gere um arquivo de saída com as linhas do primeiro seguidas da linhas do segundo arquivo.
#O nome do arquivo de saída também pode ser passado como parâmetro na linha de comando.
import sys
if len(sys.argv) != 4:
    print('Coloque 4 parametros para funcionar, por favor')
else:
    arquivo1 = open(sys.argv[1],'r')
    arquivo2 = open(sys.argv[2],'r')
    arquivofinal = open(sys.argv[3],'w')
for c in arquivo1:
    arquivofinal.write(c)
for ASM in arquivo2:
    arquivofinal.write(ASM)
arquivofinal.close()
arquivo2.close()
arquivo1.close()
