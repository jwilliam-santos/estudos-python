#Escreva um programa que aumente o preço de todos os produtos do banco preços.db em 10%
import sqlite3  as sq3

db = sq3.connect("preços.db")
cursor = db.cursor()
cursor.execute('UPDATE preços set preço  = preço* 1.1')
db.commit()