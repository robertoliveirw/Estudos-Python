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


texto_aleatorio = input('Digite no seguinte padrão: APLICAÇÃO  USUÁRIO E-MAIL SENHA')
texto_tratado = tratar_string(texto_aleatorio)
escreve_csv(texto_tratado[0], texto_tratado[1], texto_tratado[2], texto_tratado[3] )