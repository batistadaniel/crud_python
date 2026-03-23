from conexao import criar_conexao, fechar_conexao
from usuarios import inserir_usuario, selecionar_usuarios, atualizar_usuario, deletar_usuario

def menu():
    print("\n===== CRUD USUÁRIOS =====")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("0 - Sair")

def main():
    con = criar_conexao("127.0.0.1", "root", "senac", "db_teste")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            inserir_usuario(con, nome, email, senha)

        elif opcao == "2":
            selecionar_usuarios(con)

        elif opcao == "3":
            selecionar_usuarios(con)
            id = input("ID do usuário para atualizar: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            atualizar_usuario(con, id, nome, email, senha)

        elif opcao == "4":
            selecionar_usuarios(con)
            id = input("ID do usuário para deletar: ")
            deletar_usuario(con, id)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("❌ Opção inválida!")

    fechar_conexao(con)

if __name__ == "__main__":
    main()