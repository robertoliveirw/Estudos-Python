from main.main import tratar_string, escreve_sql, procura_sql

# testando funções
string_bruta = input('Digite as suas credenciais no seguinte padrão: APLICAÇÃO USUÁRIO E-MAIL SENHA \n')
print('Versão bruta: ', string_bruta)

string_tratada = tratar_string(string_bruta)
print('Sring tratada', string_tratada)

escreve_sql(*string_tratada)

print('-'*10)


procurar = input('\nDigite a aplicação desejada: ')
procura_sql(procurar)