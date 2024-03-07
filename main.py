import os


class Cores:
    CABECALHO = '\033[95m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    ALERTA = '\033[93m'
    VERMELHO = '\033[91m'
    FIM = '\033[0m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Celula:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def inserir(self, valor):
        nova_celula = Celula(valor)
        nova_celula.proximo = self.topo
        self.topo = nova_celula

    def remover(self):
        if self.estaVazia():
            print(Cores.VERMELHO + "Não existem tarefas para serem concluídas" + Cores.FIM)
            return None
        else:
            valorRemovido = self.topo.valor
            self.topo = self.topo.proximo
            return valorRemovido

    def estaVazia(self):
        return self.topo is None

    def visualizar(self):
        atual = self.topo
        indice = 1
        print(Cores.AZUL + "Tarefas pendentes:" + Cores.FIM)
        print("-----------------------------------------")
        while atual:
            print(f"{Cores.AZUL}{indice}.{Cores.FIM} {atual.valor}")
            atual = atual.proximo
            indice += 1
        print("-----------------------------------------")

def menu():
    limpar_tela()
    print(Cores.CABECALHO + "\n--- Gerenciador de Tarefas ---" + Cores.FIM)
    print(Cores.VERDE + "1. Adicionar nova tarefa" + Cores.FIM)
    print(Cores.ALERTA + "2. Concluir última tarefa" + Cores.FIM)
    print(Cores.AZUL + "3. Visualizar tarefas pendentes" + Cores.FIM)
    print(Cores.VERMELHO + "4. Sair" + Cores.FIM)
    opcao = input(Cores.CABECALHO + "Escolha uma opção: " + Cores.FIM)
    return opcao

def main():
    pilhaDeTarefas = Pilha()

    while True:
        opcao = menu()

        if opcao == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            pilhaDeTarefas.inserir(tarefa)
            print(Cores.VERDE + f"'{tarefa}' adicionada com sucesso." + Cores.FIM)
        elif opcao == '2':
            tarefaRemovida = pilhaDeTarefas.remover()
            if tarefaRemovida:
                print(Cores.ALERTA + f"Tarefa '{tarefaRemovida}' concluída." + Cores.FIM)
        elif opcao == '3':
            if pilhaDeTarefas.estaVazia():
                print(Cores.VERMELHO + "Nenhuma tarefa pendente." + Cores.FIM)
            else:
                pilhaDeTarefas.visualizar()
        elif opcao == '4':
            print(Cores.VERMELHO + "Saindo do gerenciador de tarefas..." + Cores.FIM)
            break
        else:
            print(Cores.VERMELHO + "Opção inválida! Tente novamente." + Cores.FIM)

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
