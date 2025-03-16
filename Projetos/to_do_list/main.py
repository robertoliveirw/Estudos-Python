# To do List
tarefas =  []

while True:
    controle = int(input('Digite a opção desejada: \n 1 - Ver Tarefas \n 2 - Adicionar Tarefa \n 3 - Remover Tarefa \n 4 - Salvar e sair \n'))
    match controle: 
        case 1:
            if not tarefas: 
                print("Você não tem tarefas.")
                continue
            else:  
                print("Suas tarefas são:")
                contador = 0
                for tarefa in tarefas:
                    contador += 1
                    print(f"{contador} - {tarefa}") 
                continue
        case 2: 
            adicionar_tarefa = input('Digite a tarefa:')
            print(f'Tarefa: {adicionar_tarefa} adicionada.')
            tarefas.append(adicionar_tarefa)
        case 3: 
            remover = int(input('Qual item você gostaria de remover?'))
            remover -= remover
            item_removido = tarefas.pop(remover)
            print(f'Item {item_removido} removido com sucesso.')
        case 4: 
            print('Alterações salvas. \n Saindo...4')
            break
        case _: 
            print("Erro: Opção inválida. Digite um número entre 1 e 4.")

