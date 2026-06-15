#Modifique o Programa 9.20 para que receba o nome da imagem a gerar pela linha de comando.
import sys


if len(sys.argv) != 2:
    print("Uso: python exercicio-09-42.py nome_arquivo.bmp")
    sys.exit(1)

nome_do_arquivo = sys.argv[1]


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

desenho = [
    "  rrrr r r bbbbb b    b   ggggg   g    g  r",
    "  r  r r r   b   b    b  g     g  gg   g  r",
    "  r  r r r   b   b    b  g r r g  g g  g  r",
    "  rrr   r    b   bbbbbb  g     g  g  g g  r",
    "  r     r    b   b    b  gr b rg  g  g g   ",
    "  r     r    b   b    b  g rrr g  g   gg  r",
    "  r     r    b   b    b   ggggg   g    g  r",
]

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


with open(nome_do_arquivo, "wb") as f:
    f.write(cabeçalho_bmp_binário)
    f.write(cabeçalho_dib_binário)
    f.write(dados_binário)

print(f"Arquivo {nome_do_arquivo} gerado. {largura=} x {altura=} {tamanho=} bytes")