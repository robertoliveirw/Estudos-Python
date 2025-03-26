import psycopg2

conexao = psycopg2.connect(database ="bot_senha",
                           host = "localhost",
                           user = "postgres",
                           password = '1234',
                           port = "5432"
                           )

print(conexao.info)