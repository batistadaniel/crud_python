# Isso importa a biblioteca que permite o python conversar com o mysql
import mysql.connector

# funcao para abrir conexao com o banco
def criar_conexao(host, usuario, senha, banco):
    # abre a conexao com o banco
    return mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco
    )

# funcao para fechar conexao
def fechar_conexao(con):
    # encerra a conexao com o banco
    con.close()