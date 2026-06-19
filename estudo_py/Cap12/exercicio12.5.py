#Crie um função sequências que receba qmax e qmim.
#Ela deve funcionar de forma semelhante a número, mas chamando a função sequência.
#Ela deve também funcionar quando qmim é 0, ou seja, quando a sequência é opcional.
from functools import partial


def sequência(entrada, padrão):
    posição, posição_max = 0, len(padrão)
    for caractere in entrada:
        if caractere == padrão[posição]:
            posição += 1  
        else:
            break  #
        if posição == posição_max:  #
            return 1, 0, posição - 1
    return -1, -1, -1


def sequências(entrada, padrão, qmin=1, qmax=1):
    posição = 0
    fim = -1
    achados = 0
    while posição < len(entrada):
        achou, _, ifim = sequência(entrada[posição:], padrão)
        if achou > 0:
            achados += 1
            posição += ifim + 1
            fim = posição - 1
        else:
            break
  
    if qmin == 0 and achados == 0:
        return 1, -1, -1
    elif qmin <= achados <= qmax:
        return achados, 0, fim
    else:
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


entradas = [
    "(((---)))", 
    "(((--)))",
    "(----)", 
    "----",  
    "((--))",  
    "<(((--)))>", 
    "<<(((--)))>>",
    "<<(((---)))>>",  
    "<<((--))>> <(((---)))> (((---))) ((((----))))",  # 
]

padrão = [
    partial(sequências, padrão="<", qmin=0, qmax=2),
    partial(sequências, padrão="(", qmin=3, qmax=4),
    partial(sequências, padrão="-", qmin=2, qmax=3),
    partial(sequências, padrão=")", qmin=3, qmax=4),
    partial(sequências, padrão=">", qmin=0, qmax=2),
]

for entrada in entradas:
    print("Entrada:", entrada)
    achado = False
    posição = 0
    while posição < len(entrada):
        achou, início, fim = verifica_padrão(entrada[posição:], padrão)
        if achou > 0:
            print(f"Padrão nas posições: {posição+início} a {posição+fim} ", end="")
            print("Padrão:", entrada[posição + início : posição + fim + 1])
            achado = True
            posição += fim + 1
        else:
            posição += 1
    if not achado:
        print("Nenhum padrão encontrado na entrada")
    print()
