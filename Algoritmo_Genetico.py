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

    def inicializar_populacao(self):
        """Cria a população inicial"""
        self.populacao = []
        for _ in range(self.tamanho_populacao):
            individuo = Individuo() 
            individuo.id = self.index_indiv
            self.index_indiv += 1 # Supondo que você tenha uma classe Individuo para criar novos indivíduos
            self.populacao.append(individuo)
    
    def selecao_por_torneio(self):
        """Seleciona dois indivíduos aleatoriamente e escolhe o melhor"""
        torneio = random.sample(self.populacao, 2)
        torneio.sort(key=lambda x: x.fitness(), reverse=True)  # Ordena pela pontuação (fitness)
        return torneio[0]  # Retorna o melhor

    def crossover(self, pai1, pai2):
        """Realiza o crossover de ponto único entre dois pais"""
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

    def mutacao(self, individuo):
        """Aplica mutação no indivíduo com uma certa probabilidade"""
        if random.random() < self.taxa_mutacao:
            ponto_mutacao = random.randint(0, len(individuo.cromossomos) - 1)
            individuo.cromossomos[ponto_mutacao] = 1 - individuo.cromossomos[ponto_mutacao]  # Inverte o bit

    def rodar_geracoes(self, num_geracoes):
        """Executa o algoritmo genético por um número de gerações"""
        for geracao in range(num_geracoes):
            # Calcula o fitness de todos os indivíduos na população
            for individuo in self.populacao:
                individuo.fitness()

            # Ordena a população pelos melhores fitness
            self.populacao.sort(key=lambda x: x.fitness(), reverse=True)

            # Remove os 100 piores indivíduos (os últimos após ordenação)
            self.populacao = self.populacao[:self.tamanho_populacao - self.n_melhores_to_crossover]

            # Vetor para armazenar os novos filhos
            novos_filhos = []

            # Geração de filhos a partir dos 100 melhores indivíduos
            while len(novos_filhos) < self.n_melhores_to_crossover:  # Vamos gerar apenas 100 filhos
                # Seleciona dois indivíduos para o crossover
                pai1 = random.choice(self.populacao)
                pai2 = random.choice(self.populacao)

                # Realiza o crossover
                filho1, filho2 = self.crossover(pai1, pai2)

                # Aplica a mutação
                self.mutacao(filho1)
                self.mutacao(filho2)

                # Adiciona os filhos à lista de novos filhos
                novos_filhos.append(filho1)
                novos_filhos.append(filho2)

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
                    return individuo, self.index_indiv  # Retorna o indivíduo com a solução ótima
            
            print(f"Melhor Individuo: {individuo.id} -- Geração {geracao} -- {max_pont} Pontos")

        # Caso não encontre solução, retorna o melhor indivíduo
        melhor_individuo = max(self.populacao, key=lambda x: x.fitness())
        print("Melhor solução encontrada após todas as gerações")
        return melhor_individuo, self.index_indiv
