#Utilizando a função os.walk, crie um programa que calcule o espaço ocupado por diretório e subdiretório, gerando uma página HTML com os resultados
import os
import sys

if len(sys.argv) < 2:
    print("Erro: Você precisa passar o caminho de um diretório!")
    sys.exit(1)

diretorio_inicial = sys.argv[1]
conteudo = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Análise de Espaço em Disco</title>
</head>
<body>
    <h2>Espaço Ocupado por Pasta/Subpasta:</h2>
"""
total_geral = 0
for raiz, diretorios, arquivos in os.walk(diretorio_inicial):
    tamanho_da_pasta = 0
    for f in arquivos:
        caminho_completo = os.path.join(raiz, f)
        if os.path.exists(caminho_completo):
            tamanho_da_pasta += os.path.getsize(caminho_completo)

    total_geral += tamanho_da_pasta
    tamanho_kb = tamanho_da_pasta / 1024
    conteudo += f"Diretório: <strong>{raiz}</strong> - {tamanho_kb:.2f} KB ({tamanho_da_pasta} bytes)<br>\n"
total_geral_mb = total_geral / (1024 * 1024)
conteudo += f"""<br>
    <h3><strong>Espaço Total Ocupado na Varredura: {total_geral_mb:.2f} MB</strong></h3>
</body>
</html>"""
with open("pt2ex9.36.html", "w", encoding="utf-8") as pagina:
    pagina.write(conteudo)
print("Sucesso! Análise concluída e salva em 'pt2ex9.36.html'.")