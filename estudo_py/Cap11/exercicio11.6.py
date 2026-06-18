#Escreva um programa que pergunte o nome do produto e um novo preço, Usando o banco de dados preços.db, atualize o preço desse produto no banco de dados
import sqlite3  as sq3
nome = input("Digite nome do produto ")
preco = int(input("Digite o preço do produto (esse vai ser alterado)"))
db = sq3.connect("preçosex9.6.db")
cursor = db.cursor()
cursor.execute('UPDATE preços set preço = ? WHERE nome = ?', (preco, nome))
db.commit()
