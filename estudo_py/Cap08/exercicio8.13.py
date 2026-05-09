#Escreva uma função que receba uma string com as opções válidas a aceitar ( cada opção é uma letra).
#Converta as opções válidas para letras minúsculas.
#Utilize Input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção e válida.
#Em caso de opção inválida, a função deve pedir ao usuário que digite o novamente outra opção.
#  obs:list(string) tranforma string em lista e o .join(lista)  a tranforma em string. 
strings = 'A B C Z'
def validar_string(strings):
    while True:
        resposta = 'Parabens você digitou algo, Quer um balão?'
        x = list(strings.upper())
        digitado = input('Digite uma letra entre A, B ou C ou Z').strip().upper()
        if digitado in x:
            print('Parabens você digitou algo, Quer um balão?')
            break
        else:
            print('Digite de novo')
resultado = validar_string(strings)

