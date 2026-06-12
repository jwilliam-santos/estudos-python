#Crie um programa que corrija o Programa 9.9 de forma a verificar se z existe e é um diretório.
import os 
import os.path

#if os.path.exists("z"):
#    print("O diretório z existe.")
#else:
#    print("O diretório z não existe.")

if os.path.isdir("z") == True:
    print("O diretorio 'z' existe")
else:
    print("o diretorio 'z' não existe")
    