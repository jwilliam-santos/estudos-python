#Escreva um programa que leia o nome do aluno e quatro notas.
#No final, o programa deve gravar dados lidos em um discos, usando o formato JSON.
import json
from pathlib import Path
nome = input("digite o nome do  aluno")
nota1 = int(input("Digite a nota 1"))
nota2 = int(input("Digite a nota 2"))
nota3 = int(input("Digite a nota 3"))
nota4 = int(input("Digite a nota 4"))
info = {
    "aluno" : nome,
    "notas" : [nota1,nota2,nota3,nota4]
}
with Path("pt2ex9.37.json").open("w",encoding="utf-8") as arquivo:
    json.dump(info,arquivo)