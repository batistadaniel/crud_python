import pandas as pd
import matplotlib.pyplot as plt
from conexao import criar_conexao


# cria conexão com banco
con = criar_conexao("127.0.0.1", "root", "senac", "db_teste")


# busca dados do banco e transforma em DataFrame
sql = "SELECT idade FROM usuarios"

df = pd.read_sql(sql, con)


# fecha conexão (boa prática)
con.close()


# verifica se existe dado
if df.empty:
    print("Nenhum dado para gerar gráfico.")
else:
    # gráfico de distribuição de idade
    df["idade"].plot(kind="hist")

    plt.title("Distribuição de Idade")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade")

    plt.show()