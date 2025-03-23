from main.main import tratar_string, escreve_csv, procura_csv

# testando funções
string_bruta = input('Digite as suas credenciais no seguinte padrão: APLICAÇÃO USUÁRIO E-MAIL SENHA \n')
print('Versão bruta: ', string_bruta)

string_tratada = tratar_string(string_bruta)
print('Sring tratada', string_tratada)

escreve_csv(*string_tratada)

print('-'*10)

procura_csv('clovis')