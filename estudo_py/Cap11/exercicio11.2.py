#Faça um programa para listar todos os preços do banco preços.db
import sqlite3 as sq3
db = sq3.connect("preços.db")
cursor = db.cursor()
cursor.execute("select * from preços")
resultado = cursor.fetchone()
print(f"Produto: {resultado[0]}\nPreço: {resultado[1]}")
cursor.close()
db.close()
