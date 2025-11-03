from SistemaGerenciador.Arquivo.manipulador_arquivo import salvar_tarefas, carregar_tarefas

class Lista:
    def __init__(self):
        self.lista = []
        carregar_tarefas(self)

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
            while True:
                try:
                    marcar = int(input('Digite o número da tarefa a marcar como concluída\n-> '))
                    self.lista[marcar-1] = f'[✅] {self.lista[marcar-1]}'
                    print(f"\nTarefa '{self.lista[marcar - 1]}' marcada como concluída.")
                    break
                except (ValueError, IndexError):
                    print('Erro: Digite um número válido entre 1 e', len(self.lista))

    def remover_tarefa(self):
        if not self.lista:
            print('Nenhuma tarefa adicionada ainda.')
        else:
            print('\nSuas tarefas:')
            for i, tarefa in enumerate(self.lista, start=1):
                print(f'{i}. {tarefa}')
            while True:
                try:
                    remover = int(input('Digite o número da tarefa a ser removida\n-> '))
                    if 1<= remover <= len(self.lista):
                        tarefa_removida = self.lista.pop(remover-1)
                        print(f'{tarefa_removida} foi removida da lista.')
                        break
                    else:
                        print('Erro: Digite um número válido entre 1 e', len(self.lista))
                except (ValueError, IndexError):
                    print('Erro: Digite um número válido entre 1 e', len(self.lista))

    def salvar(self):
        salvar_tarefas(self)
