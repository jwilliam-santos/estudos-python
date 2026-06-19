#Utilizando a função verifica_padrão,escreva uma função que detecte um valor em reais no formato: R$999,99 em que 9 representa qualquer dígito.
#O primeiro número pode ter um ou mais dígitos, mas a segunda parte (centavos) deve ter no máximo dois digitos
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



def opcional(entrada, padrões):
    achou, inicio, fim = verifica_padrão(entrada, padrões)
    if achou > 0:
        return achou, inicio, fim
    else:
        return 1, -1, -1


três_números = partial(número, qmin=1, qmax=3)
centavos = partial(número, qmin=1, qmax=2)
cifrão = partial(sequência, padrão="R$")
vírgula = partial(sequência, padrão=",")

padrão = [cifrão, três_números, vírgula, centavos]

entradas = [
    "R$123,45",  
    "R$123,450", 
    "$123,45", 
    "R$12,34",  
    "R$123,45 R$12,34 R$1,23 R$1,0",  
    "R$123 R$12 R$1 R$1,0",  
]
for entrada in entradas:
    print("Entrada:", entrada)
    achado = False
    posição = 0
    while posição < len(entrada):
        achou, início, fim = verifica_padrão(entrada[posição:], padrão)
        if achou > 0:
            print(f"Reais nas posições: {posição+início} a {posição+fim} ", end="")
            print("Reais:", entrada[posição + início : posição + fim + 1])
            achado = True
            posição += fim + 1
        else:
            posição += 1
    if not achado:
        print("Nenhum valor em reais encontrado na entrada")
    print()