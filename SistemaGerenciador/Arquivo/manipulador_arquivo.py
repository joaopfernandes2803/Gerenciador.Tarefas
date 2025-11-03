import pandas as pd

def salvar_tarefas(self, arquivo = 'tarefas.csv'):
    df = pd.DataFrame(self.lista, columns=['Tarefa'])
    df.to_csv(arquivo, index=False)
    print('Tarefas salvas com sucesso!')

def carregar_tarefas(self,arquivo = 'tarefas.csv'):
    try:
        df = pd.read_csv(arquivo)
        self.lista = df['Tarefa'].tolist()
        print(f'{len(self.lista)} tarefas carregadas com sucesso!')
    except FileNotFoundError:
        print('Nenhum arquivo de tarefas encontrado. Um novo será criado ao salvar.')
        self.lista = []
