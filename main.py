from Algoritmo_Genetico import AlgoritmoGenetico
import json
import Constantes


# Defina o tamanho da população e as taxas de mutação/crossover
algoritmo_genetico = AlgoritmoGenetico(tamanho_populacao=Constantes.QUANTIDADE_INDIVIDUOS, limite_pontuacao=Constantes.PONTUACAO_MAXIMA, taxa_mutacao=Constantes.TAXA_MUTACAO, taxa_crossover=Constantes.TAXA_CROSSOVER)

# Inicializa a população
algoritmo_genetico.inicializar_populacao()

# Roda o algoritmo por 100 gerações
melhor_individuo = algoritmo_genetico.rodar_geracoes(num_geracoes=Constantes.NUM_GERACOES)

best_individuo_dict = {
    "bits": ''.join(map(str, melhor_individuo.cromossomos)), 
    "resposta": melhor_individuo.resposta, 
    "pontuacao": melhor_individuo.pontuacao, 
}

# Salva o dicionário em um arquivo JSON
with open(f'Melhor_Individuo.json', 'w', encoding='utf-8') as f:
    json.dump(best_individuo_dict, f, indent=4, ensure_ascii=False)
