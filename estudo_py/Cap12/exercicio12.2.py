#Reescreva a função que mostra os números na entrada  ABC431DEF-901c431203FXEW9, mas usando a função verifica_padrão 


from functools import partial

entrada = " ABC431DEF-901c431203FXEW9"


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
        if posição == posição_max:  #
            return 1, 0, posição - 1
    return -1, -1, -1


def verifica_padrão(entrada, padrões): #Tem que mostrar  ABC431DEF-901c431203FXEW9 == entrada = 4319014312039

    tamanho = 0
    for letra in entrada:
        if  letra.isalpha() == False:
            tamanho += 1
        else:
            break    

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