import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

#cursor = conexao.cursor()
with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha ['nome'], linha ['sobrenome'])

conexao.close()
#cursor.close() CASO NAO USE O WITH