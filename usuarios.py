# importa a funcao de criar conexao do arquivo conexao.py
from conexao import criar_conexao

# funcao que insere um usuario
def inserir_usuario(con, nome, email, senha, idade, sexo):
    # cursor é um método que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "INSERT INTO usuarios (nome, email, senha, idade, sexo) VALUES (%s, %s, %s, %s, %s)"
    # dados que vao ser inseridos no banco
    valores = (nome, email, senha, idade, sexo)
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
    # cursor é um método que permite enviar comando sql
    cursor = con.cursor()
    # comando sql a ser executado
    sql = "SELECT id, nome, email, idade, sexo FROM usuarios"
    # executa a consulta
    cursor.execute(sql)
    # pega todos os resultados e guarda
    usuarios = cursor.fetchall()
    # msg de exibicao
    if len(usuarios) == 0:
        print("\n ===== Lista vazia =====")
        # fecha o cursor (isso e uma boa pratica)
        cursor.close()
        return False # retorno indicando que nao tem usuarios
    else:
        print("\n📋 Lista de usuários:")
    # percorre cada resultado
    for (id, nome, email, idade, sexo) in usuarios:
        # cada linha vira uma tupla
        print(f"{id} | {nome} | {email} | {idade} | {sexo}")
    # fecha o cursor (isso e uma boa pratica)
    cursor.close()
    return True # retorno indicando que tem usuarios

# funcao para editar um usuario
def atualizar_usuario(con, id, nome, email, senha, idade, sexo):
    
    # cursor é um método que permite enviar comando sql
    cursor = con.cursor()
    # busca os dados atuais 
    cursor.execute("SELECT nome, email, senha, idade, sexo FROM usuarios WHERE id = %s",(id,))
    # pega todos os resultados e guarda
    usuario = cursor.fetchone() 

    if not usuario:
        print("❌ Usuário não encontrado!")
        cursor.close()
        return
    
    nome_atual, email_atual, senha_atual, idade_atual, sexo_atual = usuario
    
    if not nome:
        nome = nome_atual

    if not email:
        email = email_atual

    if not senha:
        senha = senha_atual

    if not idade:
        idade = idade_atual

    if not sexo:
        sexo = sexo_atual

        
    
    # comando sql a ser executado
    sql = """
        UPDATE usuarios 
        SET nome=%s, email=%s, senha=%s, idade=%s, sexo=%s 
        WHERE id=%s
    """
    valores = (nome, email, senha, idade, sexo, id)
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
    # cursor é um método que permite enviar comando sql
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