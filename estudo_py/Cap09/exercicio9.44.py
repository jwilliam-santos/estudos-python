#Modifique o programa anterior para receber um terceiro parâmetro com a tabela de conversão de cores no formato JSON.
import sys
import json


if len(sys.argv) != 4:
    print(
        "Uso: python exercicio-09-44.py nome_arquivo_saida.bmp nome_arquivo_desenho.txt tabela_cores.json"
    )
    sys.exit(1)

arquivo_saida = sys.argv[1]
arquivo_desenho = sys.argv[2]
arquivo_cores = sys.argv[3]


try:
    with open(arquivo_desenho, "r") as f:
        desenho = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Erro: O arquivo de desenho '{arquivo_desenho}' não foi encontrado.")
    sys.exit(1)
except IOError:
    print(f"Erro: Não foi possível ler o arquivo de desenho '{arquivo_desenho}'.")
    sys.exit(1)


try:
    with open(arquivo_cores, "r") as f:
        letra_para_cor = json.load(f)
except FileNotFoundError:
    print(f"Erro: O arquivo de cores '{arquivo_cores}' não foi encontrado.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{arquivo_cores}' não contém um JSON válido.")
    sys.exit(1)


for caractere in letra_para_cor:
    cor = letra_para_cor[caractere]
    if len(cor) != 3 or not all(isinstance(x, int) and 0 <= x <= 255 for x in cor):
        print(f"Erro: Cor inválida para o caractere '{caractere}'")
        sys.exit(1)


def bytes_little_endian(número, nbytes=4, sinal=False):
    """Converte um número inteiro para uma sequência de bytes usando a codificação little endian.
    Se sinal for passado, reserva um bit para representar o sinal."""
    return número.to_bytes(nbytes, "little", signed=sinal)


def padding(valor, tamanho=4):
    """Calcula o próximo múltiplo para tamanho"""
    if resto := valor % tamanho:
        return valor + tamanho - resto
    return valor


multiplicador = 32


largura_desenho = len(desenho[0])

for linha, z in enumerate(desenho):
    if len(z) != largura_desenho:
        raise ValueError(
            f"Linhas devem ter o mesmo tamanho. Linha com largura diferente: {linha} em vez de {len(z)}"
        )


desenho_expandido = []
for linha in desenho:
    nova_linha = []
    for letra in linha:
        nova_linha.append(letra * multiplicador)
    for _ in range(multiplicador):
        desenho_expandido.append("".join(nova_linha))


largura = len(desenho_expandido[0])  
altura = len(desenho_expandido)  #


dados_binário = []
for linha in desenho_expandido:
    linha_binária = []
    for caractere in linha:
    
        linha_binária.append(bytes(letra_para_cor[caractere][::-1]))
    dados_binário.append(b"".join(linha_binária))

largura_bytes = largura * 3
largura_com_padding = padding(largura_bytes)
if largura_bytes != largura_com_padding:
    for p, d in enumerate(dados_binário):
        dados_binário[p] = b"".join(
            [dados_binário[p], bytes(largura_com_padding - largura_bytes)]
        )


tamanho = padding(largura * 3) * altura

cabeçalho_bmp = [
    b"BM",  
    bytes_little_endian(54 + tamanho), 
    bytes(4),  
    bytes_little_endian(54),  
]

cabeçalho_dib = [
    bytes_little_endian(40),  
    bytes_little_endian(largura),
    bytes_little_endian(
        -altura, sinal=True
    ),  
    bytes_little_endian(1, 2), 
    bytes_little_endian(24, 2),  
    bytes_little_endian(0),  
    bytes_little_endian(tamanho),
    bytes_little_endian(2835),  
    bytes_little_endian(2835),  
    bytes_little_endian(0),  
    bytes_little_endian(0),  
]
cabeçalho_bmp_binário = b"".join(cabeçalho_bmp)
cabeçalho_dib_binário = b"".join(cabeçalho_dib)
dados_binário = b"".join(dados_binário)

assert len(cabeçalho_bmp_binário) == 14
assert len(cabeçalho_dib_binário) == 40
assert len(dados_binário) == tamanho



with open(arquivo_saida, "wb") as f:
    f.write(cabeçalho_bmp_binário)
    f.write(cabeçalho_dib_binário)
    f.write(dados_binário)

print(f"Arquivo {arquivo_saida} gerado. {largura=} x {altura=} {tamanho=} bytes")