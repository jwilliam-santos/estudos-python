
import sqlite3

dados = [("João", "98901-0109"), ("André", "98902-8900"), ("Maria", "97891-3321")]
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.executemany(
    """
      insert into agenda (nome, telefone)
      values(?, ?)
      """,
    dados,
)
conexão.commit()
cursor.close()
conexão.close()