#Faça um Programa que crie o banco de dados "preço.db" com a tabela preçros para armazenar uma lista de preços de venda de produtos.
#A tabela deve conter o nome do produto e seu respectivo preço.
#O programa também deve inserir alguns dados para teste
import sqlite3 as sq3
db = sq3.connect("preços.db")
cursor = db.cursor()
cursor.execute("""
        create table preços(
            nome text,
            preço int)
        """)
cursor.execute(
    """
        insert into preços (nome ,preço )
            values(?, ?)
            """,
    ("Celular", "500"),
)
db.commit()
cursor.close()
db.close()