import random

class Processo:
    lista_processos = []
    
    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        self.texec = tempo_execucao
        self.techagada = tempo_chegada
        self.prioridade = prioridade
        self.tempo_execucao_original = tempo_execucao

    @classmethod
    def exibir_funcionamento_fcfs(cls): 
        for processo in cls.lista_processos:
            processo.texec = processo.tempo_execucao_original
            
        tempo = 1
        tempos_espera = []
        
        for indice, processo in enumerate(cls.lista_processos):
            while processo.texec > 0:
                processo.texec -= 1
                print(f'tempo[{tempo}]: processo[{indice}] restante={processo.texec}')
                tempo += 1
        
        tempo_atual = 1
        for indice, processo in enumerate(cls.lista_processos):
            tempo_espera = tempo_atual - 1  
            tempos_espera.append(tempo_espera)
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')
            tempo_atual += processo.tempo_execucao_original
        
        media_espera = sum(tempos_espera) / len(tempos_espera)
        print(f'Tempo médio de espera: {media_espera}')

    @classmethod
    def exibir_sjf_nao_preemptivo(cls):
        for processo in cls.lista_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos = cls.lista_processos[:]
        tempos_espera = []
        concluidos = 0
        total = len(processos)

        print('\n--- SJF Não Preemptivo ---\n')

        while concluidos < total:
            disponiveis = []

            for processo in processos:
                if processo.techagada <= tempo and processo.texec > 0:
                    disponiveis.append(processo)

            if len(disponiveis) == 0:
                tempo += 1
                continue

            atual = disponiveis[0]
            for processo in disponiveis:
                if processo.texec < atual.texec:
                    atual = processo

            indice = cls.lista_processos.index(atual)

            tempo_espera = tempo - atual.techagada
            tempos_espera.append(tempo_espera)

            while atual.texec > 0:
                atual.texec -= 1
                print(f'tempo[{tempo}]: processo[{indice}] restante={atual.texec}')
                tempo += 1

            concluidos += 1

        media = sum(tempos_espera) / len(tempos_espera)
        print(f'\nTempo médio de espera: {media}')

    @classmethod
    def exibir_sjf_preemptivo(cls):
        for processo in cls.lista_processos:
            processo.texec = processo.tempo_execucao_original

        tempo = 0
        processos = cls.lista_processos[:]
        n = len(processos)
        concluidos = 0
        tempos_espera = [0] * n

        print('\n--- SJF Preemptivo ---\n')

        while concluidos < n:
            indice_escolhido = -1
            menor_tempo = None

            for i in range(n):
                processo = processos[i]
                if processo.techagada <= tempo and processo.texec > 0:
                    if menor_tempo is None or processo.texec < menor_tempo:
                        menor_tempo = processo.texec
                        indice_escolhido = i

            if indice_escolhido == -1:
                tempo += 1
                continue

            atual = processos[indice_escolhido]

            print(f'tempo[{tempo}]: processo[{indice_escolhido}] restante={atual.texec - 1}')
            atual.texec -= 1
            tempo += 1

            if atual.texec == 0:
                concluidos += 1
                tempo_final = tempo
                tempo_espera = tempo_final - atual.techagada - atual.tempo_execucao_original
                tempos_espera[indice_escolhido] = tempo_espera

        media = sum(tempos_espera) / n
        print(f'\nTempo médio de espera: {media}')

    @classmethod
    def exibir_processos_criados(cls):
        print('\n--- Processos Criados ---')
        for indice, processo in enumerate(cls.lista_processos):
            print(f'Processo[{indice}]: tempo_execucao={processo.tempo_execucao_original} tempo_chegada={processo.techagada} prioridade={processo.prioridade}')
        print()

    @classmethod
    def criacao_processo_via_input(cls, quantidade_processos):
        for indice in range(quantidade_processos):
            print(f'\n--- Processo {indice} ---')
            novo_processo = cls(
                int(input('Digite o tempo de execução: ')), 
                int(input('Digite o tempo de chegada: ')), 
                int(input('Digite o nível de prioridade: '))
            )
            cls.lista_processos.append(novo_processo)
        
        print('\nProcessos criados com sucesso.')
        cls.exibir_processos_criados()

    @classmethod
    def criacao_aleatorio(cls):
        numero_processos_aleatorio = 3
        for indice in range(numero_processos_aleatorio):
            novo_processo = cls(
                random.randint(1, 10),
                random.randint(0, 10),
                random.randint(1, 10)
            )
            cls.lista_processos.append(novo_processo)
        
        print(f'\n{numero_processos_aleatorio} processos criados com sucesso.')
        cls.exibir_processos_criados()


class Sistema:
    def menu(self):
        continuar = True

        while continuar:
            print('\n-_-_-_- Programa de Escalonamento -_-_-_-\n'
                  '\n[0] Criar Processos Manualmente\n'
                  '[1] Criar Processos Aleatoriamente\n'
                  '[2] Executar Escalonamento FCFS\n'
                  '[3] Executar SJF\n'
                  '[4] Excluir Processos\n'
                  '[5] Sair\n'
                  '\n-_-_-_- Programa de Escalonamento -_-_-_-\n')
            
            opcao = input('\nDigite aqui: ')

            match opcao:
                case '0':
                    if Processo.lista_processos:
                        print('\nExistem processos já cadastrados. Deseja excluí-los?')
                        resp = input('Digite S para sim ou N para não: ').upper()
                        if resp == 'S':
                            Processo.lista_processos.clear()
                            quantidade = int(input('\nQuantos processos serão criados? '))
                            Processo.criacao_processo_via_input(quantidade)
                        else:
                            print('\nOperação cancelada.')
                    else:
                        quantidade = int(input('\nQuantos processos serão criados? '))
                        Processo.criacao_processo_via_input(quantidade)

                case '1':
                    if Processo.lista_processos:
                        print('\nExistem processos já cadastrados. Deseja excluí-los?')
                        resp = input('Digite S para sim ou N para não: ').upper()
                        if resp == 'S':
                            Processo.lista_processos.clear()
                            Processo.criacao_aleatorio()
                        else:
                            print('\nOperação cancelada.')
                    else:
                        Processo.criacao_aleatorio()

                case '2':
                    if Processo.lista_processos:
                        print('\n--- Executando FCFS ---\n')
                        Processo.exibir_funcionamento_fcfs()
                    else:
                        print('\nNão há processos cadastrados.')

                case '3':
                    if Processo.lista_processos:
                        print('\nEscolha o tipo de SJF:\n'
                              '[1] Não Preemptivo\n'
                              '[2] Preemptivo\n')
                        
                        tipo = input('Digite: ')

                        if tipo == '1':
                            Processo.exibir_sjf_nao_preemptivo()
                        elif tipo == '2':
                            Processo.exibir_sjf_preemptivo()
                        else:
                            print('\nOpção inválida.')
                    else:
                        print('\nNão há processos cadastrados.')

                case '4':
                    if Processo.lista_processos:
                        Processo.lista_processos.clear()
                        print('\nProcessos excluídos.')
                    else:
                        print('\nNenhum processo cadastrado.')

                case '5':
                    continuar = False
                    print('\nPrograma encerrado.')

                case _:
                    print('\nOpção inválida.')


if __name__ == '__main__':
    sistema = Sistema()
    sistema.menu()