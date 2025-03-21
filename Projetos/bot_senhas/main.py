import csv

def tratar_string(texto):
    palavras = texto.split()
    
    texto1 = palavras[0] if len(palavras) > 0 else ""
    texto2 = palavras[1] if len(palavras) > 1 else ""
    texto3 = palavras[2] if len(palavras) > 2 else ""
    texto4 = palavras[3] if len(palavras) > 3 else ""
    
    return texto1, texto2, texto3, texto4

def escreve_csv(texto1, texto2, texto3, texto4):
    with open('database/initial_database.csv','a', newline='') as csvfile:
        escrever = csv.writer(csvfile, delimiter=';')
        escrever.writerow([texto1, texto2, texto3, texto4])

def procura_csv(aplicacao):
    with open('database/initial_database.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for linha in reader:
            if linha and aplicacao in linha[0]: 
                app, usuario, email, senha = linha[:4] 
                return f"Aplicativo: {app}\nUsuário: {usuario}\nE-mail: {email}\nSenha: {senha}"
    return f"Nenhum aplicativo encontrado para: {aplicacao}"