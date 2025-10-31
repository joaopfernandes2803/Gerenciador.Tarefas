def salvar_tarefas(self,arquivo = 'tarefas.txt'):
    with open(arquivo,'w', encoding='utf-8') as arquivo:
        for tarefa in self.lista:
            arquivo.write(tarefa +'\n')
    print('Tarefas salvas com sucesso!')

def carregar_tarefas(self,arquivo = 'tarefas.txt'):
    try:
        with open(arquivo,'r', encoding = 'utf-8') as arquivo:
            self.lista = [linha.strip() for linha in arquivo.readlines()]
        print('Tarefas carregadas com sucesso!')
    except FileNotFoundError:
        print('Nenhum arquivo de tarefas encontrado. Foi criado um arquivo com sucesso.')
        self.lista = []