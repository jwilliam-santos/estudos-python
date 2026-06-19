#Programa Util nos exercicios 12.2 a 12.6
from functools import partial

entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."


def número(entrada, qmin, qmax):
    num = 0
    for caractere in entrada:
        if caractere.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return num, 0, num - 1
    else:
        return -1, -1, -1


def sequência(entrada, padrão):
    posição, posição_max = 0, len(padrão)
    for caractere in entrada:
        if caractere == padrão[posição]:
            posição += 1  # Caracteres iguais, testa o próximo caractere
        else:
            break  # Saiu da sequência
        if posição == posição_max:  # Achou toda a sequência
            return 1, 0, posição - 1
    return -1, -1, -1


def verifica_padrão(entrada, padrões):
    posição = 0
    for padrão in padrões:
        achou, _, fim = padrão(entrada[posição:])
        if achou > 0:
            posição += fim + 1
        else:
            return -1, -1, -1
    return 1, 0, posição - 1


def ddd(entrada):
    achou, _, fim = verifica_padrão(
        entrada,
        [
            partial(sequência, padrão="("),
            partial(número, qmin=2, qmax=3),
            partial(sequência, padrão=")"),
        ],
    )
    return (1, 0, fim) if achou > 0 else (-1, -1, -1)


for posição in range(len(entrada)):
    achou, início, fim = ddd(entrada[posição:])
    if achou > 0:
        print(f"DDD encontrado nas posições: {posição+início} a {posição+fim}")
        print(entrada[posição + início : posição + fim + 1])