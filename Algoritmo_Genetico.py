import random
from Individuo import Individuo

class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao, limite_pontuacao, taxa_mutacao, taxa_crossover, n_crossover_melhores):
        self.tamanho_populacao = tamanho_populacao
        self.limite_pontuacao = limite_pontuacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.n_melhores_to_crossover = n_crossover_melhores
        self.populacao = []
        self.index_indiv = 0
        self.total_fitness = 0
        self.roleta = []


    def inicializar_populacao(self):
       
        self.populacao = []
        for _ in range(self.tamanho_populacao):
            individuo = Individuo() 
            individuo.id = self.index_indiv
            self.index_indiv += 1 # Supondo que você tenha uma classe Individuo para criar novos indivíduos
            self.populacao.append(individuo)

    def crossover(self, pai1, pai2):
      
        if random.random() < self.taxa_crossover:
            ponto_crossover = random.randint(1, len(pai1.cromossomos) - 1)
            filho1 = pai1.cromossomos[:ponto_crossover] + pai2.cromossomos[ponto_crossover:]
            filho2 = pai2.cromossomos[:ponto_crossover] + pai1.cromossomos[ponto_crossover:]
            f1 = Individuo(filho1)
            f1.id = self.index_indiv
            self.index_indiv += 1
            f2 = Individuo(filho2)
            f2.id = self.index_indiv
            self.index_indiv += 1
            return f1, f2
        else:
            return pai1, pai2  # Se não ocorrer crossover, retorna os pais
        
    def calculate_fitness_population(self):
        self.total_fitness = 0
        self.total_fitness = sum(individuo.fitness() for individuo in self.populacao)
        self.calculate_roleta()

    def calculate_roleta(self):
        self.roleta = []
        probabilidade_acumulada = 0
        
        for individuo in self.populacao:
            if self.total_fitness!= 0:
                probabilidade = individuo.pontuacao / self.total_fitness
                probabilidade_acumulada += probabilidade
                self.roleta.append(probabilidade_acumulada)

    def selecao_por_roleta(self):
        pais_selecionados = []

        while len(pais_selecionados) < self.n_melhores_to_crossover:
            #print("Gerando pais")
            sorteio = random.random()  # Gera um número aleatório entre 0 e 1
            for i, probabilidade in enumerate(self.roleta):
                if sorteio <= probabilidade:
                    pais_selecionados.append(self.populacao[i])
                    break

        return pais_selecionados
    
    def selecao_por_torneio(self):
        pais_selecionados = []
        while len(pais_selecionados) < self.n_melhores_to_crossover:
                # Seleciona dois indivíduos para o crossover
                pai1 = random.choice(self.populacao)
                pai2 = random.choice(self.populacao)

                pais_selecionados.append(pai1)
                pais_selecionados.append(pai2)
        
        return pais_selecionados
            
    def mutacao(self, individuo):
      
        if random.random() < self.taxa_mutacao:
            ponto_aleatorio = random.randint(0,24)
            tipo_mutacao = random.randint(0,1)
            if tipo_mutacao == 1:
                for i in range(3):
                    #INVERTE
                    individuo.cromossomos[ponto_aleatorio * 3 + i] = 1 - individuo.cromossomos[ponto_aleatorio * 3 + i]  # Inverte o bit
            else:
                #SOMA UMA UNIDADE
                for i in range(2, -1, -1):
                    if individuo.cromossomos[ponto_aleatorio * 3 + i] == 0:
                        individuo.cromossomos[ponto_aleatorio * 3 + i] = 1
                        break
                    else:
                        individuo.cromossomos[ponto_aleatorio * 3 + i] = 0
                        

    
    def rodar_geracoes(self, num_geracoes):
        
        for geracao in range(num_geracoes):

            #print(len(self.populacao))

            #Calcula o Fitness total necessario para a seleção por roleta e e já atualiza o fitness de cada individuo
            self.calculate_fitness_population()

            # Ordena a população pelos melhores fitness
            self.populacao.sort(key=lambda x: x.pontuacao, reverse=True)

            pais_selecionados = self.selecao_por_torneio()

            # Vetor para armazenar os novos filhos
            novos_filhos = []

            # Geração de filhos a partir dos n pais selecionados 
            for i in range(0, len(pais_selecionados) - 1, 2):
                pai1 = pais_selecionados[i]
                pai2 = pais_selecionados[i+1]
                filho1, filho2 = self.crossover(pai1, pai2)
                filho1.geracao = geracao
                filho2.geracao = geracao

                # Aplica a mutação
                self.mutacao(filho1)
                self.mutacao(filho2)

                novos_filhos.append(filho1)
                novos_filhos.append(filho2)

            #REMOVE OS n piores    
            self.populacao = self.populacao[:self.tamanho_populacao - self.n_melhores_to_crossover]

            # Adiciona os novos filhos à população
            self.populacao.extend(novos_filhos)

            # Verifica se algum indivíduo atingiu a pontuação limite
            max_pont = self.populacao[0].fitness()
            max_index = 0
            #print(len(self.populacao))
            for index, individuo in enumerate(self.populacao):
                if individuo.fitness() > max_pont:
                    max_pont = individuo.pontuacao
                    
                if individuo.fitness() >= self.limite_pontuacao:
                    print(f"Solução encontrada na geração {geracao}")
                    individuo.translate_resposta()
                    return individuo, self.index_indiv
            
            print(f"Melhor Individuo: {individuo.id} -- Geração {geracao} -- {max_pont} Pontos")

        # Caso não encontre solução, retorna o melhor indivíduo
        melhor_individuo = max(self.populacao, key=lambda x: x.fitness())
        print("Melhor solução encontrada após todas as gerações")
        melhor_individuo.translate_resposta()
        return melhor_individuo, self.index_indiv
