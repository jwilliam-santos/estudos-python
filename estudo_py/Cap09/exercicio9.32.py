#Modifique o Programa 9.9 de forma a receber o nome do arquivo ou diretório a verificar pela linha de comando. 
#Imprima se existir e se for um arquivo ou um diretório.
import sys
import os.path
diretorio = sys.argv[1]
if os.path.exists(diretorio) == True:
    print("O arquivo/diretorio Existe")
else:
    print("O arquivo não existe")