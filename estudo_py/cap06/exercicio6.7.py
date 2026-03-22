#Faça um programa que leia uma expressão com parênteses. 
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
#Exemplo:
#(()) OK
#()()(()()) OK
#()) Erro
#Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses.
#Ao desempilhar, verifique se o topo da pilha é um abre parênteses. 
#Se a expressão estiver correta, sua pilha estará vazia no final
#programa começa na proxíma linha (11)
parenteses = input('Digite os parenteses a validar:')
x = 0
pilha = []
while x < len(pilha):
    if parenteses[x] == '(':
        pilha.append('(')
    if parenteses[x] == ')':
        if len(pilha ) >0:
            z = pilha.pop(-1)
        else:
            pilha.append(')')
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")