class Lista:
    def __init__(self):
        self.lista = []

    def adicionar_tarefas(self):
        adicionar = input('Adicionar tarefa\n-> ')
        self.lista.append(adicionar)
        print(f'{adicionar} foi adicionado à sua lista.')

    def listar_tarefas(self):
        if not self.lista:
            print('Nenhuma tarefa adicionada ainda.')
        else:
            print('\nSuas tarefas:')
            for i, tarefa in enumerate(self.lista, start=1):
                print(f'{i}. {tarefa}')

    def marca_tarefa(self):
        if not self.lista:
            print('Nenhuma tarefa adicionada ainda.')
        else:
            print('\nSuas tarefas:')
            for i, tarefa in enumerate(self.lista, start=1):
                print(f'{i}. {tarefa}')

        marcar = int(input('Digite o número da tarefa a marcar como concluída\n-> '))
        self.lista[marcar-1] = f'[✅]{self.lista[marcar-1]}'
        print(f'Tarefa{self.lista[marcar-1]}  marcada como concluída.')

    def remover_tarefa(self):
        if not self.lista:
            print('Nenhuma tarefa adicionada ainda.')
        else:
            print('\nSuas tarefas:')
            for i, tarefa in enumerate(self.lista, start=1):
                print(f'{i}. {tarefa}')
        remover = int(input('Digite o número da tarefa a ser removida\n-> '))
        if 1<= remover <= len(self.lista):
            tarefa_removida = self.lista.pop(remover-1)
            print(f'{tarefa_removida} foi removido da lista.')

    def salvar_carregar_tarefas(self):
        pass
