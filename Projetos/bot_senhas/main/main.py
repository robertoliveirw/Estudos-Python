import csv

def tratar_string(texto):
    palavras = texto.split()
    
    aplicacao = palavras[0] if len(palavras) > 0 else ""
    usuario = palavras[1] if len(palavras) > 1 else ""
    email = palavras[2] if len(palavras) > 2 else ""
    senha = palavras[3] if len(palavras) > 3 else ""
    
    return aplicacao, usuario, email, senha

def escreve_csv(aplicacao, usuario, email, senha):
    with open('database/initial_database.csv', 'a', newline='', encoding='utf-8') as csvfile:
        escrever = csv.writer(csvfile, delimiter=';')
        escrever.writerow([aplicacao, usuario, email, senha])

def procura_csv(aplicacao_desejada):
    with open('database/initial_database.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for linha in reader:
            if linha and aplicacao_desejada in linha[0]: 
                aplicacao, usuario, email, senha = linha[:4] 
                return print(f"Aplicativo: {aplicacao}\nUsuário: {usuario}\nE-mail: {email}\nSenha: {senha}")