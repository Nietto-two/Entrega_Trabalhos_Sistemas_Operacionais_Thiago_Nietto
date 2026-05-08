import random

class Processo:
    
    lista_de_processos = []

    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        self.texec = tempo_execucao
        self.techegada = tempo_chegada
        self.prioridade = prioridade
        self.tempo_execucao_original = tempo_execucao
        
    @classmethod
    def criar_processos_aleatorios(cls):
        for processos in range(3):
            novo_processo = cls(random.randint(1, 10),
                                random.randint(1, 10),
                                random.randint(1, 10))
            
            cls.lista_de_processos.append(novo_processo)

        cls.exibir_lista_de_processos()

    @classmethod
    def criar_processos_manualmente(cls):
        quantidade_de_processos = int(input('\nQuantos processos deseja criar? '))

        for processos in range(quantidade_de_processos):
            novo_processo = cls(int(input('\nDigite o tempo de execução: ')), 
                                int(input('Digite o tempo de chegada: ')), 
                                int(input('Digite o nível de prioridade: ')))
            
            cls.lista_de_processos.append(novo_processo)
        
        cls.exibir_lista_de_processos()

    @classmethod
    def escalonamento_fcfs(cls):
        for processo in cls.lista_de_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 1
        lista_com_tempo_de_espera = []

        for indice, processo in enumerate(cls.lista_de_processos):
            while processo.texec > 0:
                processo.texec -= 1
                print(f'tempo[{tempo}]: processo[{indice}] restante={processo.texec}')
                tempo += 1

        tempo_atual = 1

        for indice, processo in enumerate(cls.lista_de_processos):
            tempo_espera = tempo_atual -1
            lista_com_tempo_de_espera.append(tempo_espera)
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')
            tempo_atual += processo.tempo_execucao_original

        tempo_medio_de_espera = sum(lista_com_tempo_de_espera) / len(lista_com_tempo_de_espera)
        print(f'Tempo médio de espera: {tempo_medio_de_espera}\n')       

    @classmethod
    def escalonamento_sjf_nao_preemptivo(cls):
        for processo in cls.lista_de_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos_restantes = cls.lista_de_processos[:]
        tempos_de_espera = {}

        while processos_restantes:
            prontos = []
            for processo in processos_restantes:
                if processo.techegada <= tempo:
                    prontos.append(processo)

            if len(prontos):
                print(f'tempo[{tempo}]: nenhum processo está pronto.')
                tempo += 1
                continue

            processo_atual = prontos[0]
            for processo in prontos:
                if processo.texec < processo_atual.texec:
                    processo_atual = processo

            indice = cls.lista_de_processos.index(processo_atual)

            tempos_de_espera[indice] = tempo - processo_atual.techegada

            while processo_atual.texec > 0:
                print(f'tempo[{tempo}]: processo[{indice}] restante={processo_atual.texec}')
                processo_atual.texec -= 1
                tempo += 1
            processos_restantes.remove(processo_atual)

        for indice, tempo_espera in tempos_de_espera.items():
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')

        tempo_medio = sum(tempos_de_espera.values()) / len(tempos_de_espera)
        print(f'Tempo médio de espera: {tempo_medio}\n')


    @classmethod
    def escalonamento_sjf_preemptivo(cls):
        for processo in cls.lista_de_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos_restantes = cls.lista_de_processos[:]
        tempos_de_conclusao = {}

        while processos_restantes:
            prontos = []
            for processo in processos_restantes:
                if processo.techegada <= tempo:
                    prontos.append(processo)

            if len(prontos) == 0:
                print(f'tempo[{tempo}]: nenhum processo está pronto.')
                tempo += 1
                continue

            processo_atual = prontos[0]
            for processo in prontos:
                if processo.texec < processo_atual.texec:
                    processo_atual = processo

            indice = cls.lista_de_processos.index(processo_atual)

            print(f'tempo[{tempo}]: processo[{indice}] restante={processo_atual.texec}')
            processo_atual.texec -= 1
            tempo += 1

            if processo_atual.texec == 0:
                processos_restantes.remove(processo_atual)
                tempos_de_conclusao[indice] = tempo

        for indice, tempo_conclusao in tempos_de_conclusao.items():
            processo = cls.lista_de_processos[indice]
            tempo_espera = tempo_conclusao - processo.techegada - processo.tempo_execucao_original
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')

        total_espera = 0
        for indice in tempos_de_conclusao:
            processo = cls.lista_de_processos[indice]
            total_espera += tempos_de_conclusao[indice] - processo.techegada - processo.tempo_execucao_original

        tempo_medio = total_espera / len(tempos_de_conclusao)
        print(f'Tempo médio de espera: {tempo_medio}\n')

    @classmethod
    def escalonamento_prioridade_preemptivo(cls):
        for processo in cls.lista_de_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos_restantes = cls.lista_de_processos[:]
        tempos_de_conclusao = {}

        while processos_restantes:
            prontos = []
            for processo in processos_restantes:
                if processo.techegada <= tempo:
                    prontos.append(processo)

            if not prontos:
                print(f'tempo[{tempo}]: nenhum processo está pronto.')
                tempo += 1
                continue

            processo_atual = prontos[0]
            for processo in prontos:
                if processo.prioridade < processo_atual.prioridade:
                    processo_atual = processo

            indice = cls.lista_de_processos.index(processo_atual)

            print(f'tempo[{tempo}]: processo[{indice}] restante={processo_atual.texec}')
            processo_atual.texec -= 1
            tempo += 1

            if processo_atual.texec == 0:
                processos_restantes.remove(processo_atual)
                tempos_de_conclusao[indice] = tempo

        for indice, tempo_conclusao in tempos_de_conclusao.items():
            processo = cls.lista_de_processos[indice]
            tempo_espera = tempo_conclusao - processo.techegada - processo.tempo_execucao_original
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')

        total_espera = 0
        for indice in tempos_de_conclusao:
            processo = cls.lista_de_processos[indice]
            total_espera += tempos_de_conclusao[indice] - processo.techegada - processo.tempo_execucao_original

        print(f'Tempo médio de espera: {total_espera / len(tempos_de_conclusao)}\n')

    @classmethod
    def escalonamento_prioridade_nao_preemptivo(cls):
        for processo in cls.lista_de_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos_restantes = cls.lista_de_processos[:]
        tempos_de_espera = {}

        while processos_restantes:
            prontos = []
            for processo in processos_restantes:
                if processo.techegada <= tempo:
                    prontos.append(processo)

            if not prontos:
                print(f'tempo[{tempo}]: nenhum processo está pronto.')
                tempo += 1
                continue

            processo_atual = prontos[0]
            for processo in prontos:
                if processo.prioridade < processo_atual.prioridade:
                    processo_atual = processo

            indice = cls.lista_de_processos.index(processo_atual)
            tempos_de_espera[indice] = tempo - processo_atual.techegada

            while processo_atual.texec > 0:
                print(f'tempo[{tempo}]: processo[{indice}] restante={processo_atual.texec}')
                processo_atual.texec -= 1
                tempo += 1

            processos_restantes.remove(processo_atual)

        for indice, tempo_espera in tempos_de_espera.items():
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')

        tempo_medio = sum(tempos_de_espera.values()) / len(tempos_de_espera)
        print(f'Tempo médio de espera: {tempo_medio}\n')

    @classmethod
    def escalonamento_round_robin(cls):
        pass

    @classmethod
    def exibir_lista_de_processos(cls):
        for indice, processo in enumerate(cls.lista_de_processos):
            print(f'Processo[{indice}]: tempo_execucao={processo.tempo_execucao_original} tempo_chegada={processo.techegada} prioridade={processo.prioridade}')
        print()

    @classmethod
    def popular_processos_novamente(cls):
        Processo.lista_de_processos.clear()
        
        resposta = input('Escolha uma das opções abaixo:\n' \
                    '[0] Criar processos aleatórios\n' \
                    '[1] Criar processos manualmente\n')

        match resposta:
            case '0':
                cls.criar_processos_aleatorios()

            case '1':
                cls.criar_processos_manualmente()

class Sistema:
    def menu_inicial(self):
        continuar = True

        while continuar:
            opcao = input('\n-_-_-_- Programa de Escalonamento -_-_-_-\n'
            '\nSelecione uma das opções abaixo:\n' \
            '[0] Criar processos\n' \
            '[1] Sair\n'
            '\n-_-_-_- Programa de Escalonamento -_-_-_-\n')

            match opcao:
                case '0':
                    resposta = input('\nEscolha uma das opções abaixo:\n' \
                    '[0] Criar processos aleatórios\n' \
                    '[1] Criar processos manualmente\n')

                    match resposta:
                        case '0':
                            Processo.criar_processos_aleatorios()
                            Sistema.menu_escalonamentos()

                        case '1':
                            Processo.criar_processos_manualmente()
                            Sistema.menu_escalonamentos()

                case '1':
                    print('Encerrando...\n')
                    continuar = False

                case _:
                    print('Opção inválida. Digite novamente.\n')

    @classmethod
    def menu_escalonamentos(cls):
        opcao = ''
        while opcao != '9':
            opcao = input('Selecione uma das opções abaixo:\n' \
            '[1] FCFS\n' \
            '[2] SJF preemptivo\n' \
            '[3] SJF não preemptivo\n' \
            '[4] Prioridade preemptivo\n' \
            '[5] Prioridade não preemptivo\n' \
            '[6] Round Robin\n' \
            '[7] Imprime lista de processos\n' \
            '[8] Popular processos novamente\n' \
            '[9] Voltar ao menu inicial\n')

            match opcao:
                case '1':
                    Processo.escalonamento_fcfs()
                case '2':
                    Processo.escalonamento_sjf_preemptivo()
                case '3':
                    Processo.escalonamento_sjf_nao_preemptivo()
                case '4':
                    Processo.escalonamento_prioridade_preemptivo()
                case '5':
                    Processo.escalonamento_prioridade_nao_preemptivo()
                case '6':
                    Processo.escalonamento_round_robin()
                case '7':
                    Processo.exibir_lista_de_processos()
                case '8':
                    Processo.popular_processos_novamente()
                case '9':
                    print()
                case _:
                    print('Opção inválida. Digite novamente.\n')

if __name__ == '__main__':
    sistema = Sistema()
    sistema.menu_inicial()
