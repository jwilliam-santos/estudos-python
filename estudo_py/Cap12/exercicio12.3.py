#Utilizando a função verifica_padrão,escreva  uma função que detecte uma data no formado dd/mm/aa em que dd e o dia, mm o mês e aa o ano.
#A função deve apenas detectar o padrão da data e não verificar se ela é valida
from functools import partial


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
            posição += 1  
        else:
            break  
        if posição == posição_max:  
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


dois_números = partial(número, qmin=2, qmax=2)
barra = partial(sequência, padrão="/")
padrão = [dois_números, barra, dois_números, barra, dois_números]


entradas = [
    "12/03/24", 
    "12/3/2024", 
    "Dia doze de março 12/03",  
    "12-03-24 12/03/2024 abc 21/30/24",  
    "12/03/24 12/03/624 abc 21/30/24", 
]
for entrada in entradas:

    print("Entrada:", entrada)
    achado = False
    posição = 0
    while posição < len(entrada):
        achou, início, fim = verifica_padrão(entrada[posição:], padrão)
        if achou > 0:
            print(f"Data posições: {posição+início} a {posição+fim} ", end="")
            print("Data:", entrada[posição + início : posição + fim + 1])
            achado = True
            posição += fim + 1
        else:
            posição += 1
    if not achado:
        print("Nenhuma data encontrada na entrada")
    print()