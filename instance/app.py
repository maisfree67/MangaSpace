import sqlite3

con = sqlite3.connect("banco.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT,
    admin BOOLEAN DEFAULT 0
)
""")
cur.execute("""
    CREATE TABLE manga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    descricao TEXT,
    capa TEXT,
    genero TEXT,
    capitulo INTEGER
)
""")
con.commit()
con.close()