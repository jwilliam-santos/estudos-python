#Escreva um programa que compare duas listas.
#Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
#Utilizando operações com conjuntos , seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# os elementos que não mudaram
# os novos elementos 
# os elementos que foram removidos
lista_inicial = ["tomate", "batata", "feijão", "alface"]
lista_alterada = ["tomate", "batata", "cebola", "arroz"]
inicial = set(lista_inicial)
alterada = set(lista_alterada)
nao_mudaram = inicial & alterada
novos = alterada - inicial
removidos = inicial - alterada
print(f"Não mudaram: {nao_mudaram}")
print(f"Novos elementos: {novos}")
print(f"Elementos removidos: {removidos}")