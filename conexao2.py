import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='senac',
    database='db_teste'
)

cursor = conexao.cursor()

id = input("Digite o id: ")
nome = input("Digite o nome: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")

sql = f"UPDATE usuarios SET nome='{nome}', email='{email}', senha='{senha}' WHERE id='{id}'" #(nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')

cursor.execute(sql)
conexao.commit()

cursor.close()