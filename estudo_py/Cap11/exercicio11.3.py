#Escreva um programa que realize consultas do banco de dados preços.db, criado no Exercício 11.1. O programa deve perguntar o nome do produto e listar seu preço
import sqlite3 as sq3

nome = input("digite o nome do produto que você quer procurar no banco de dados 'preços.db':")
db = sq3.connect("preços.db")
cursor = db.cursor()
cursor.execute(f'select * from preços where nome = ?',(nome,))
while True:
    x = cursor.fetchone()
    if x is None:
        break
    print(f"Nome:{x[0]}\n Preço {x[1]}")
cursor.close()
db.close()