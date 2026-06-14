#Modifique o programa anterios para que leia o mesmo arquivo, permitindo adicionar mais dados ao arquivo.
#Se o mesmo nome for  digitado duas vezes, altere os dados para a nova entrada.
import json
from pathlib import Path
import os.path
addnome = []
notas = []

while True:
    
    nome = input("digite o nome do  aluno").strip().lower()
    if nome != "sair":
            addnome.append(nome)
    if nome == "sair":
            break
        
    while True:
        print("Digite as notas, Para sair digite sair, antes de sair se for alterar algo digite limpar para resetar ")
        nota = (input("Digite as notas")).strip().lower()
        if nota != "sair":
             notas.append(nota)
        if nota == "sair":
                
                break
        if nota == "limpar":
              notas.clear()
if len(addnome) >= 1:
    addnome.pop(0)
    if len(addnome) != len(set(addnome)):
          notas.clear()
info = {
    "aluno" : addnome,
    "notas": notas
}
arquivojson = input("Qual o nome do arquivo json? Digite o nome mesmo se ele não existir, digite ele com a extensão .json se existir ")

if os.path.exists(arquivojson):
        with open(arquivojson) as arquivo:
           info =  json.load(arquivo)
else:
    with Path(arquivojson).open("w",encoding="utf-8") as arquivo:
        json.dump(info,arquivo)
        
