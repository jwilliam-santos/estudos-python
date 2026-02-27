#modiofique o programa anterior para que aceite respostas com letras maiusculas e minusculas
#pontos = 0
# questao = 1
# while questao <= 3:
#   respostas = input(f'resposta questao{questao}')
#   if questao == 1 and resposta == 'b':
#   pontos = pontos + 1
# if questao == 2 and resposta == 'a' 
#   pontos = pontos + 1
# questao = questao + 1
#print(f'o alunos fez {pontos} pontos(s)')
pontos = 0
questao = 1
while questao <= 3:
    respostas = input(f'Resposta questao {questao}')
    if questao == 1 and (respostas == 'b' or respostas == 'B'):
        pontos = pontos + 1
    if questao == 2 and (respostas== 'a'  or respostas == 'A'):
        pontos = pontos + 1 
    if questao == 3 and (respostas == 'd' or respostas == 'D'):
        pontos = pontos + 1
    questao += 1
print(f'o alunos fez {pontos} pontos(s)')


