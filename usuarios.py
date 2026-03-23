from conexao import criar_conexao

# CREATE
def inserir_usuario(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)

    cursor.execute(sql, valores)
    con.commit()
    cursor.close()

    print("✅ Usuário cadastrado com sucesso!")

# READ
def selecionar_usuarios(con):
    cursor = con.cursor()
    sql = "SELECT id, nome, email FROM usuarios"

    cursor.execute(sql)

    print("\n📋 Lista de usuários:")
    for (id, nome, email) in cursor:
        print(f"{id} | {nome} | {email}")

    cursor.close()

# UPDATE
def atualizar_usuario(con, id, nome, email, senha):
    cursor = con.cursor()
    sql = "UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE id=%s"
    valores = (nome, email, senha, id)

    cursor.execute(sql, valores)
    con.commit()
    cursor.close()

    print("🔄 Usuário atualizado com sucesso!")

# DELETE
def deletar_usuario(con, id):
    cursor = con.cursor()
    sql = "DELETE FROM usuarios WHERE id=%s"

    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()

    print("🗑️ Usuário deletado com sucesso!")