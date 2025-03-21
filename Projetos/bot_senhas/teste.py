from main.main import tratar_string, escreve_csv, procura_csv

# testando funções
aplicacao, usuario, email, senha = tratar_string("Facebook user123 email@example.com pass123")
print(aplicacao, usuario, email, senha)

escreve_csv(aplicacao, usuario, email, senha)
procura_csv('facebook')
