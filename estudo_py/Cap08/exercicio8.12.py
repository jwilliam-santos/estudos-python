#Escreva uma função que receba uma string e uma lista.
#A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
#Retorne Verdadeito se a string for encrontrada dentro da lista, e falso, caso contrário.
def stringLista(string, lista):
    if string in lista:
        return True
    else:
        return False
print(stringLista('Olá',['Ola','BomDia','Olá']))