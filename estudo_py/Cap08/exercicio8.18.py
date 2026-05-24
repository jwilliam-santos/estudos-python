#Modifique o Programa 8.26 para que receba dois parâmetros opcionais.
#Um para indicar o caractere a imprimir antes do número, sendo o espaço em branco o valor padrão, caso este não seja passado.
#O segundo parâmetro opcional é quantos caracteres adcionar por nível, tendo 2 como valor padrão.
#----------------------------------------------------------------------------------------------------------------------------
#def imprime_listas(lista, nível=0):
#    for x in lista:
#        if isinstance(x, int):
#            print(f"{x:{nível * 2}}")
#        else:
#            imprime_listas(x, nível + 1)
#O programa começa na proxíma linha (12)
def imprime_listas(lista, nível=0, caractere = ' ', quant=2, recuo = 0):
    recuo = caractere * (nível * quant)
    for x in lista:
        if isinstance(x, int):
            print(f"{caractere * (nível * quant)}{x}")
        else:
            imprime_listas(x,nível+1,caractere,quant)

imprime_listas([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10], caractere="*", quant=4)