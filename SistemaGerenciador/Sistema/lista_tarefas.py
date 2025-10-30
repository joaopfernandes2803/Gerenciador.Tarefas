class Lista:
    def __init__(self):
        self.lista = []

    def adicionar_tarefas(self):
        adicionar = input('Adicionar tarefa\n-> ')
        self.lista.append(adicionar)
        print(f'{adicionar} foi adicionado à sua lista.')

    def listar_tarefas(self):
        if not self.lista:
            print("Nenhuma tarefa adicionada ainda.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(self.lista, start=1):
                print(f"{i}. {tarefa}")

    def marca_tarefa(self):
        pass

    def remover_tarefa(self):
        pass

    def salvar_carregar_tarefas(self):
        pass
