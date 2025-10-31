from SistemaGerenciador.Sistema.lista_tarefas import Lista

if __name__ == '__main__':
    sistema = Lista()

    while True:
        print('-'*30)
        print('GERENCIADOR DE TAREFAS'.center(30))
        print('-'*30)
        print('\n1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Marca tarefa')
        print(f'4 - Remover tarefa')
        print('6 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            sistema.adicionar_tarefas()
        elif opcao == '2':
            sistema.listar_tarefas()
        elif opcao == '3':
            sistema.marca_tarefa()
        elif opcao == '4':
            sistema.remover_tarefa()
        elif opcao == '6':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida!')
