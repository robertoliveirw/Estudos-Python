import cryptocode
import psycopg2

def tratar_string(texto):
    palavras = texto.split()
    
    aplicacao = palavras[0] if len(palavras) > 0 else ""
    usuario = palavras[1] if len(palavras) > 1 else ""
    email = palavras[2] if len(palavras) > 2 else ""
    senha = palavras[3] if len(palavras) > 3 else ""

    encripted_usuario = cryptocode.encrypt(usuario, password='12345')
    encripted_email = cryptocode.encrypt(email, password='12345')
    encripted_senha = cryptocode.encrypt(senha, password='12345')
    
    return aplicacao, encripted_usuario, encripted_email, encripted_senha

def escreve_sql(aplicacao, encripted_usuario, encripted_email, encripted_senha):
    try:
        # Conectar no Banco de Dados
        conexao = psycopg2.connect(
            database ="bot_senha",
            host = "localhost",
            user = "postgres",
            password = '1234',
            port = "5432"
        )
        
        cursor = conexao.cursor()
        query = """
        INSERT INTO senhas_db_1 (aplicacao, usuario, email, senha)
        VALUES (%s, %s, %s, %s);
        """

        cursor.execute(query, (aplicacao, encripted_usuario, encripted_email, encripted_senha))
        conexao.commit()
        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def procura_sql(aplicacao_desejada):
    try:
        # Conectar ao banco de dados
        conexao = psycopg2.connect(
            database="bot_senha",
            host="localhost",
            user="postgres",
            password="1234",
            port="5432"
        )

        cursor = conexao.cursor()

        query = """
        SELECT aplicacao, usuario, email, senha 
        FROM senhas_db_1
        WHERE LOWER(aplicacao) = LOWER(%s);
        """

        cursor.execute(query, (aplicacao_desejada,))
        resultado = cursor.fetchone()
    
        if resultado:
            aplicacao, encripted_usuario, encripted_email, encripted_senha = resultado
            usuario = cryptocode.decrypt(encripted_usuario, password='12345')
            email = cryptocode.decrypt(encripted_email, password='12345')
            senha = cryptocode.decrypt(encripted_senha, password='12345')

            print(f"Aplicativo: {aplicacao}\nUsuário: {usuario}\nE-mail: {email}\nSenha: {senha}")
        else:
            print(f"Aplicação '{aplicacao_desejada}' não encontrada.")

        cursor.close()
        conexao.close()

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
