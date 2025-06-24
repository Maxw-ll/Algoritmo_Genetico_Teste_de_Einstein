import random
from Individuo import Individuo

class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao, limite_pontuacao, taxa_mutacao, taxa_crossover):
        self.tamanho_populacao = tamanho_populacao
        self.limite_pontuacao = limite_pontuacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.populacao = []

    def inicializar_populacao(self):
        """Cria a população inicial"""
        self.populacao = []
        for _ in range(self.tamanho_populacao):
            individuo = Individuo()  # Supondo que você tenha uma classe Individuo para criar novos indivíduos
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
            return Individuo(filho1), Individuo(filho2)
        else:
            return pai1, pai2  # Se não ocorrer crossover, retorna os pais

    def mutacao(self, individuo):
        """Aplica mutação no indivíduo com uma certa probabilidade"""
        if random.random() < self.taxa_mutacao:
            ponto_mutacao = random.randint(0, len(individuo.cromossomos) - 1)
            individuo.cromossomos[ponto_mutacao] = 1 - individuo.cromossomos[ponto_mutacao]  # Inverte o bit

    def substituicao(self):
        """Substitui os piores indivíduos com os melhores filhos"""
        self.populacao.sort(key=lambda x: x.fitness(), reverse=True)  # Ordena pela pontuação
        # A substituição pode ocorrer da forma que preferir, como substituir os piores com os filhos
        filhos = self.populacao[-len(self.populacao)//2:]  # Assume que os piores são a metade inferior
        for i in range(len(filhos)):
            self.populacao[i] = filhos[i]

    def rodar_geracoes(self, num_geracoes):
        """Executa o algoritmo genético por um número de gerações"""
        for geracao in range(num_geracoes):
            print(f"Geração {geracao}")
            nova_populacao = []
            while len(nova_populacao) < self.tamanho_populacao:
                # Seleciona os pais
                pai1 = self.selecao_por_torneio()
                pai2 = self.selecao_por_torneio()

                # Realiza o crossover
                filho1, filho2 = self.crossover(pai1, pai2)

                # Aplica a mutação
                self.mutacao(filho1)
                self.mutacao(filho2)

                # Adiciona os filhos à nova população
                nova_populacao.append(filho1)
                nova_populacao.append(filho2)

            # Substitui a população antiga pela nova
            self.populacao = nova_populacao
            self.substituicao()

            # Verifica se algum indivíduo atingiu a pontuação limite
            for individuo in self.populacao:
                if individuo.fitness() >= self.limite_pontuacao:
                    print(f"Solução encontrada na geração {geracao}")
                    return individuo  # Retorna o indivíduo com a solução ótima

        # Caso não encontre solução, retorna o melhor indivíduo
        melhor_individuo = max(self.populacao, key=lambda x: x.fitness())
        print("Melhor solução encontrada após todas as gerações")
        return melhor_individuo
