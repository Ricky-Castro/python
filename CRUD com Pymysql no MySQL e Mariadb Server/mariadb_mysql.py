import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='@hdc*1111',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('')
        print('Conexão fechada!')
        conexao.close()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = ('INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'
#                '(%s, %s, %s, %s)')
#         cursor.execute(sql, ('Jack', 'Smith', 112, 220))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = ('INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'
#                '(%s, %s, %s, %s)')
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('MAURO', 'ROBERTISON', 80, 55.5),
#             ('ADRIANO', 'MANUEL', 83, 69),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id = %s"
#         cursor.execute(sql, (7,))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id IN (%s, %s, %s)"
#         cursor.execute(sql, (5, 8, 10))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "UPDATE clientes SET sobrenome=%s WHERE id=%s"
#         cursor.execute(sql, ('SMITH', 6))
#         conexao.commit()

#cursor = conexao.cursor()
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER By id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
            #print(linha ['nome'], linha ['sobrenome'])

#conexao.close()
#cursor.close() CASO NAO USE O WITH