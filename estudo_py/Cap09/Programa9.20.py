#Este programa sera importante nos exercicio 9.42 a 9.44
ARQUIVO = "imagem_python.bmp"


def bytes_little_endian(número, nbytes=4, sinal=False):
    """Converte um número inteiro para uma sequência de bytes usando a codificação little endian.
    Se sinal for passado, reserva um bit para representar o sinal."""
    return número.to_bytes(nbytes, "little", signed=sinal)


def padding(valor, tamanho=4):
    """Calcula o próximo múltiplo para tamanho"""
    if resto := valor % tamanho:
        return valor + tamanho - resto
    return valor


# Tabela de conversão de letra para cor
# no formato RGB (red, green, blue)
# Cada cor pode variar de 0 a 255.
letra_para_cor = {
    " ": (0, 0, 0),  # preto
    "r": (255, 0, 0),  # vermelho
    "g": (0, 255, 0),  # verde
    "b": (0, 0, 255),  # azul
}
# Desenho que vamos transformar em imagem
desenho = [
    "  rrrr r r bbbbb b    b   ggggg   g    g  r",
    "  r  r r r   b   b    b  g     g  gg   g  r",
    "  r  r r r   b   b    b  g r r g  g g  g  r",
    "  rrr   r    b   bbbbbb  g     g  g  g g  r",
    "  r     r    b   b    b  gr b rg  g  g g   ",
    "  r     r    b   b    b  g rrr g  g   gg  r",
    "  r     r    b   b    b   ggggg   g    g  r",
]
# Multiplicador de pontos
# Cada ponto será copiado multiplicador vezes na imagem
# Se igual a 4, cada ponto gera um bloco de 4x4 pontos
multiplicador = 32

# Checa se todas as linhas têm o mesmo tamanho
largura_desenho = len(desenho[0])

for linha, z in enumerate(desenho):
    if len(z) != largura_desenho:
        raise ValueError(
            f"Linhas devem ter o mesmo tamanho. Linha com largura diferente: {linha} em vez de {len(z)}"
        )

# Calcula os dados com base no multiplicador
desenho_expandido = []
for linha in desenho:
    nova_linha = []
    for letra in linha:
        nova_linha.append(letra * multiplicador)
    for _ in range(multiplicador):
        desenho_expandido.append("".join(nova_linha))


largura = len(desenho_expandido[0])  # Número de colunas na imagem
altura = len(desenho_expandido)  # Número de linhas na imagem

# Checa se as letras representam as cores
dados_binário = []
for linha in desenho_expandido:
    linha_binária = []
    for caractere in linha:
        # Inverte a ordem dos bytes para o formato RGB do bmp
        linha_binária.append(bytes(letra_para_cor[caractere][::-1]))
    dados_binário.append(b"".join(linha_binária))

# Adiciona o padding
largura_bytes = largura * 3
largura_com_padding = padding(largura_bytes)
if largura_bytes != largura_com_padding:
    for p, d in enumerate(dados_binário):
        dados_binário[p] = b"".join(
            [dados_binário[p], bytes(largura_com_padding - largura_bytes)]
        )

# Calcula o tamanho em bytes da imagem com o padding
tamanho = padding(largura * 3) * altura

cabeçalho_bmp = [
    b"BM",  # Identificador
    bytes_little_endian(54 + tamanho),  # Tamanho da imagem em bytes
    bytes(4),  # 4 bytes 0x00
    bytes_little_endian(54),  # Tamanho dos cabeçalhos
]

cabeçalho_dib = [
    bytes_little_endian(40),  # Tamanho do cabeçalho DIB
    bytes_little_endian(largura),
    bytes_little_endian(
        -altura, sinal=True
    ),  # Altura negativa para montar a imagem de cima para baixo
    bytes_little_endian(1, 2),  # Planos de cor
    bytes_little_endian(24, 2),  # Bits por ponto
    bytes_little_endian(0),  # Sem compressão
    bytes_little_endian(tamanho),
    bytes_little_endian(2835),  # teto(72 dpi x 39.3701 pol/m) horizontal
    bytes_little_endian(2835),  # teto(72 dpi x 39.3701 pol/m) vertical
    bytes_little_endian(0),  # Número de cores na palete
    bytes_little_endian(0),  # Cores importantes
]

cabeçalho_bmp_binário = b"".join(cabeçalho_bmp)
cabeçalho_dib_binário = b"".join(cabeçalho_dib)
dados_binário = b"".join(dados_binário)

# Verifica o tamanho de cada cabeçalho binário
assert len(cabeçalho_bmp_binário) == 14
assert len(cabeçalho_dib_binário) == 40
assert len(dados_binário) == tamanho

# Grava a imagem
with open(ARQUIVO, "wb") as f:
    f.write(cabeçalho_bmp_binário)
    f.write(cabeçalho_dib_binário)
    f.write(dados_binário)

print(f"Arquivo {ARQUIVO} gerado. {largura=} x {altura=} {tamanho=} bytes")