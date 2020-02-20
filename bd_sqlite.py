import sqlite3


conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

"""
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
"""
"""
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'João', 'peso': 90}
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Joseph', 'peso': 70}
)
conexao.commit()
"""
"""
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Manuel', 'id': 5}
)
conexao.commit()
"""
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 3}
)
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)


cursor.close()
conexao.close()