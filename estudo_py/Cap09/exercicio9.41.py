#Altere o programa visualiza.py (programa9.18) para receber o número máximo de bytes a imprimir e quantos bytes por linha pela linha de comando.
import sys
import itertools


def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {" " * 3 * (bytes_por_linha - len(b))}{tview}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python programa.py arquivo max_bytes bytes_por_linha")
        sys.exit(1)

    arquivo = sys.argv[1]
    max_bytes = int(sys.argv[2])
    bytes_por_linha = int(sys.argv[3])

    with open(arquivo, "rb") as f:
        imagem = f.read(max_bytes)

    imprime_bytes(imagem, bytes_por_linha)
