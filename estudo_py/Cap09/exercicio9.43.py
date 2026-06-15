#Modifique o programa do exercício anterior para receber um segundo parâmetro com o nome do arquivo com o desenho. 
#A ideia é ler o desenho desse arquivo.
import sys


if len(sys.argv) != 3:
    print(
        "Uso: python exercicio-09-43.py nome_arquivo_saida.bmp nome_arquivo_desenho.txt"
    )
    sys.exit(1)

arquivo_saida = sys.argv[1]
arquivo_desenho = sys.argv[2]


try:
    with open(arquivo_desenho, "r") as f:
        desenho = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Erro: O arquivo de desenho '{arquivo_desenho}' não foi encontrado.")
    sys.exit(1)
except IOError:
    print(f"Erro: Não foi possível ler o arquivo de desenho '{arquivo_desenho}'.")
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



letra_para_cor = {
    " ": (0, 0, 0),  
    "r": (255, 0, 0), 
    "g": (0, 255, 0),  
    "b": (0, 0, 255),  
}


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
altura = len(desenho_expandido)  

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