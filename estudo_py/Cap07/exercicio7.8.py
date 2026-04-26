#Escreva um programa para exibir todas as palavras de uma frase. 
#Considere que uma palavra termina com um espaço em branco ou quando a string terminar.
#Exemplo: “O rato roeu a roupa” deve imprimir 5.
frase =input('Digite uma frase: ')
palavras = frase.split(' ')
print(len(palavras))