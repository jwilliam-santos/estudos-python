#utilizando a função os.walk, crie uma página HTML como nome e tamanho de cada arquivo de um diretório passado e de seus subdiretórios
# Garante que o programa não vai quebrar se você esquecer de passar a pasta no terminal
import os
import sys
if len(sys.argv) < 2:
    print("Erro: Você precisa passar o caminho de um diretório!")
    print("Exemplo: python script.py /caminho/da/pasta")
    sys.exit(1)

diretorio = sys.argv[1]


conteudo = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Pt2ex9.35</title>
</head>
<body>
    <h2>Lista de Arquivos Encontrados:</h2>
"""

for raiz, diretorios, arquivos in os.walk(diretorio):
    for f in arquivos:
     
        caminho_completo = os.path.join(raiz, f)
       
        tamanho = os.path.getsize(caminho_completo)
        
        
        conteudo += f"Arquivo: <strong>{f}</strong> - Tamanho: {tamanho} bytes<br>\n"

conteudo += """</body>
</html>"""

with open("pt2ex9.35.html", "w", encoding="utf-8") as pagina:
    pagina.write(conteudo)

print("Sucesso! O arquivo 'pt2ex9.35.html' foi gerado com todos os dados.")
        