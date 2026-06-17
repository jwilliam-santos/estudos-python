import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchone()
print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexão.close()