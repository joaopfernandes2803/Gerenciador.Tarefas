from SistemaGerenciador.Sistema.lista_tarefas import Lista

if __name__ == "__main__":
    sistema = Lista()

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            sistema.adicionar_tarefas()
        elif opcao == "2":
            sistema.listar_tarefas()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")
