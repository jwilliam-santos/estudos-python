#Modifique o Programa anterior para reconhecer sequências de letras.
#Uma letra é um caractere entre A e Z ou entre a e z, considerando letras maiúsculas e minúsculas.
#Ignore caracteres acentuados. 
#Imprima uma lista com as sequências de letras encontradas:

entrada = "ABC431DEF901c431203FXEW9"
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
saída = []
letra = []
for caractere in entrada:
    if caractere in alfabeto:
        if not letra:
            saída.append(letra)
        letra += caractere
    elif letra:
        letra = []
for encontrado in saída:
    print("".join(encontrado))