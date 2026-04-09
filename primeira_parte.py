import random

class Processo:
    lista_processos = []
    
    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        self.texec = tempo_execucao
        self.techagada = tempo_chegada
        self.prioridade = prioridade
        self.tempo_execucao_original = tempo_execucao

    def exibir_funcionamento_fcfs(self): 
        for processo in Processo.lista_processos:
            processo.texec = processo.tempo_execucao_original
            
        tempo = 1
        tempos_espera = []
        
        for indice, processos in enumerate(Processo.lista_processos):
            while processos.texec > 0:
                processos.texec -= 1
                print(f'tempo[{tempo}]: processo[{indice}] restante={processos.texec}')
                tempo += 1
        
        tempo_atual = 1
        for indice, processos in enumerate(Processo.lista_processos):
            tempo_espera = tempo_atual - 1  
            tempos_espera.append(tempo_espera)
            print(f'Processo[{indice}]: tempo_espera={tempo_espera}')
            tempo_atual += processos.tempo_execucao_original
        
        media_espera = sum(tempos_espera) / len(tempos_espera)
        print(f'Tempo médio de espera: {media_espera}')

    def exibir_processos_criados(self):
        print('\n--- Processos Criados ---')
        for indice, processos in enumerate(Processo.lista_processos):
            print(f'Processo[{indice}]: tempo_execucao={processos.tempo_execucao_original} tempo_chegada={processos.techagada} prioridade={processos.prioridade}')
        print()

    @classmethod
    def criacao_processo_via_input(cls, quantidade_processos):
        for processos in range(quantidade_processos):
            print(f'\n--- Processo {processos} ---')
            novo_processo = Processo(int(input('Digite o tempo de execução: ')), 
                                     int(input('Digite o tempo de chegada: ')), 
                                     int(input('Digite o nível de prioridade: ')))
            Processo.lista_processos.append(novo_processo)
        
        print('\nProcessos criados com sucesso.')
        temp_processo = Processo(0, 0, 0)
        temp_processo.exibir_processos_criados()

    @classmethod
    def criacao_aleatorio(cls):
        numero_processos_aleatorio = random.randint(1, 10)
        for processos in range(numero_processos_aleatorio):
            novo_processo = Processo(random.randint(1, 10),
                                     random.randint(0, 10),
                                     random.randint(1, 10))
            Processo.lista_processos.append(novo_processo)
        
        print(f'\n{numero_processos_aleatorio} processos criados com sucesso.')
        temp_processo = Processo(0, 0, 0)
        temp_processo.exibir_processos_criados()

class Sistema:
    def menu(self):
        continuar = True

        while continuar:
            print('\n-_-_-_- Programa de Escalonamento -_-_-_-\n'
                  '\n[0] Criar Processos Manualmente\n'
                  '[1] Criar Processos Aleatoriamente\n'
                  '[2] Executar Escalonamento FCFS\n'
                  '[3] Excluir Processos\n'
                  '[4] Sair\n'
                  '\n-_-_-_- Programa de Escalonamento -_-_-_-\n')
            
            opcao = input('\nDigite aqui: ')

            match opcao:
                case '0':
                    if Processo.lista_processos:
                        print('\nExistem processos já cadastrados. Deseja excluí-los?')
                        resp = input('Digite S para sim ou N para não: ').upper()
                        if resp == 'S':
                            Processo.lista_processos.clear()
                            quantidade_processos = int(input('\nQuantos processos serão criados? '))
                            Processo.criacao_processo_via_input(quantidade_processos)
                        else:
                            print('\nOperação cancelada.')
                    else:
                        quantidade_processos = int(input('\nQuantos processos serão criados? '))
                        Processo.criacao_processo_via_input(quantidade_processos)

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
                        print('\n--- Executando Escalonamento FCFS ---\n')
                        processo_temp = Processo(0, 0, 0)
                        processo_temp.exibir_funcionamento_fcfs()
                    else: 
                        print('\nNão há processos cadastrados. Crie processos primeiro (opção 0 ou 1).')

                case '3':
                    if Processo.lista_processos:
                        Processo.lista_processos.clear()
                        print('\nPronto! Os processos cadastrados foram excluídos.')
                    else:
                        print('\nAinda não há nenhum processo cadastrado.')

                case '4':
                    continuar = False
                    print('\nPrograma encerrado.')
                
                case _:
                    print('\nOpção inválida.\n')
    
sistema = Sistema()
sistema.menu()