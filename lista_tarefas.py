tarefas = []  #lista onde todas as tarefas estão guardadas   
historico = []   #permite que as tarefas sejam desfeitas      
fila_execucao = []   #lista de espera para as tarefas que ainda não foram atendidas   

def adicionar_tarefa(tarefa): #adiciona a tarefa nas três listas acima
    tarefas.append(tarefa)#adiciona as tarefas a lista principal
    historico.append(tarefa)#adiciona a tarefa ao historico 
    fila_execucao.append(tarefa)#adiciona a lista de espera
    print(f"Tarefa '{tarefa}' adicionada!\n")

def desfazer_tarefa():#remove uma tarefa expecifica da lista
    if tarefas:#verifica se há tarefas na lista principal
        mostrar_tarefas()#mostra ao usuario as tarefas que estão na lista
        entrada = input("Digite o número da tarefa que deseja remover: ")
        if entrada.isdigit():#verifica se o usuário digitou um numero
            indice = int(entrada) - 1#ajusta o número para condizer com a posição da tarefa
            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)#remove da lista principal 
                if removida in historico:
                    historico.remove(removida)#remove do historico 
                if removida in fila_execucao:
                    fila_execucao.remove(removida)#remove da lista de espera
                print(f"Tarefa '{removida}' removida!\n")
            else:
                print("Número inválido.\n")
        else:
            print("Entrada inválida. Digite apenas números.\n")
    else:
        print("Nenhuma tarefa para remover.\n")
        
def atender_tarefa():#atende uma tarefa expecifica
    if tarefas:
        mostrar_tarefas()#mostra ao usuario as tarefas que estão na lista
        entrada = input("Digite o número da tarefa que deseja atender: ")#numero da tarefa que o usuário quer atender
        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(tarefas):
                feita = tarefas.pop(indice)
                if feita in fila_execucao:
                    fila_execucao.remove(feita)
                if feita in historico:
                    historico.remove(feita)
                print(f"Tarefa '{feita}' atendida!\n")
            else:
                print("Número inválido.\n")
        else:
            print("Entrada inválida. Digite apenas números.\n")
    else:
        print("Nenhuma tarefa para atender.\n")
def mostrar_tarefas():#mostra as tarefas com indice para facilitar a vida do usuario
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):#mostra as tarefas com enumeração 
        print(f"{i + 1}. {t}")
    print()

def arquivo_texto():#cria um arquivo de texto com as tarefas adicionadas na lista
    with open('tarefas.txt', 'w') as f:
        for tarefa in tarefas:
            f.write(f'Tarefas: {tarefa}\n')
    print("Arquivo 'tarefas.txt' criado com sucesso!\n")


while True:#interface
    print("1. Adicionar Tarefa")
    print("2. Desfazer Tarefa")
    print("3. Atender Tarefa")
    print("4. Mostrar Tarefas")
    print("5. criar arquivo de texto com as tarefas")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")
    #mecanismos da interface
    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        desfazer_tarefa()
    elif opcao == '3':
        atender_tarefa()
    elif opcao == '4':
        mostrar_tarefas()
    elif opcao == '7':
        print(historico)
    elif opcao == '5':
        arquivo_texto()
    elif opcao == '6':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!\n")