#Crie um programa que gere uma página HTML com links para todos os arquivos jpg e png encontrados a partir de um diretório informado na linha de comando.
import sys
import os.path
import os
with open ("pt2ex9.33.html","w") as arquivo:
        imagens = sys.argv[1]
        arquivo.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>algo</title>
</head>
<body>
""")    
        a = os.path.exists(imagens)
        if imagens.lower().endswith(".jpg") or imagens.lower().endswith(".png"):
            arquivo.write(f'<a href="{arquivo}">{arquivo}</a>\n')