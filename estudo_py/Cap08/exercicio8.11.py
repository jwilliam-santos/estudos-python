#Escreva uma função para validar uma variável string.
#Essa função recebe como parâmetro a string, o número mínimo e o máximo de caracteres.
#Retorne VERDADEIRO se o tamanho da string estiver estre o valores máximo e mínimo.
def validar_tamanho(txt,min,máx):
    x = len(txt)
    if min < x and x < máx:
        return  True
    else:
        return False
print(validar_tamanho("computador", 3, 15))  
print(validar_tamanho("oi", 5, 10))           
print(validar_tamanho("estudando", 1, 5))    