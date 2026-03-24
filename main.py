# Importando funcoes
from conexao import criar_conexao, fechar_conexao
from usuarios import inserir_usuario, selecionar_usuarios, atualizar_usuario, deletar_usuario

# menu
def menu():
    print("\n===== CRUD USUÁRIOS =====")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("0 - Sair")

# funcao principal
def main():
    # cria a conexao
    con = criar_conexao("127.0.0.1", "root", "senac", "db_teste")

    # mantem o programa rodando ate sair
    while True:
        # chama o menu sempre no inicio
        menu()
        # pega a opcao que o usuario digitou
        opcao = input("Escolha uma opção: ")

        # se opcao for 1, chama a funcao de inserir usuario
        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            inserir_usuario(con, nome, email, senha)

        # se opcao for 2, chama a funcao de listar usuario
        elif opcao == "2":
            selecionar_usuarios(con)

        # se opcao for 3, chama a funcao de atualizar usuario
        elif opcao == "3":
            selecionar_usuarios(con)
            id = input("ID do usuário para atualizar: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            atualizar_usuario(con, id, nome, email, senha)

        # se opcao for 4, chama a funcao de deletar usuario
        elif opcao == "4":
            selecionar_usuarios(con)
            id = input("ID do usuário para deletar: ")
            deletar_usuario(con, id)

        # se opcao for 0, encerra o programa
        elif opcao == "0":
            print("Encerrando...")
            break

        # quando a desgraca do usuario digitar uma opcao invalida 
        else:
            print("❌ Opção inválida!")

    # fecha conexao
    fechar_conexao(con)

# garante que o programa so roda qunado for executado diretamente
if __name__ == "__main__":
    main()