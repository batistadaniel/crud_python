# importa a funcao de criar conexao do arquivo conexao.py
from conexao import criar_conexao

# funcao que insere um usuario
def inserir_usuario(con, nome, email, senha):
    # cursor e o que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    # dados que vao ser inseridos no banco
    valores = (nome, email, senha)
    # executa o comando sql com os dados
    cursor.execute(sql, valores)
    # commit salva no banco
    con.commit()
    # fecha o cursor (isso e uma boa pratica)
    cursor.close()
    # msg
    print("✅ Usuário cadastrado com sucesso!")

# funcao que ler usuarios
def selecionar_usuarios(con):
    # cursor e o que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "SELECT id, nome, email FROM usuarios"
    # executa a consulta
    cursor.execute(sql)
    # msg de exibicao
    print("\n📋 Lista de usuários:")
    # percorre cada resultado
    for (id, nome, email) in cursor:
        # cada linha vira uma tupla
        print(f"{id} | {nome} | {email}")
    # fecha o cursor (isso e uma boa pratica)
    cursor.close()

# funcao para editar um usuario
def atualizar_usuario(con, id, nome, email, senha):
    # cursor e o que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE id=%s"
    valores = (nome, email, senha, id)
    # executa o comando sql com os dados
    cursor.execute(sql, valores)
    # commit salva no banco
    con.commit()
    # fecha o cursor (isso e uma boa pratica)
    cursor.close()
    # msg
    print("🔄 Usuário atualizado com sucesso!")

# funcao para excluir um funcionario
def deletar_usuario(con, id):
    # cursor e o que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "DELETE FROM usuarios WHERE id=%s"
    # executa o comando sql com os dados
    cursor.execute(sql, (id,))
    # commit salva no banco
    con.commit()
    # fecha o cursor (isso e uma boa pratica)
    cursor.close()
    # msg
    print("🗑️ Usuário deletado com sucesso!")