from Algoritmo_Genetico import AlgoritmoGenetico
from Individuo import Individuo
import json
import Constantes
import time


def show_individuo(path_json: str):

    with open(path_json, 'r', encoding='utf-8') as f:
        indiv_dict = json.load(f)

    aux_indv = Individuo()

    aux_indv.resposta = indiv_dict['resposta']

    aux_indv.imprimir_resposta()


def run_genetic():
    # Defina o tamanho da população e as taxas de mutação/crossover
    algoritmo_genetico = AlgoritmoGenetico(tamanho_populacao=Constantes.QUANTIDADE_INDIVIDUOS, limite_pontuacao=Constantes.LIMITE_ACEITAVEL, taxa_mutacao=Constantes.TAXA_MUTACAO, taxa_crossover=Constantes.TAXA_CROSSOVER, n_crossover_melhores=Constantes.QUANTIDADE_CORTE_MELHORES)

    # Inicializa a população
    algoritmo_genetico.inicializar_populacao()
    print("População Iniciada!")

    # Roda o algoritmo por 100 gerações
    begin = time.time()
    melhor_individuo, total_individuos = algoritmo_genetico.rodar_geracoes(num_geracoes=Constantes.NUM_GERACOES)
    end = time.time()


    best_individuo_dict = {
        "bits": ''.join(map(str, melhor_individuo.cromossomos)), 
        "resposta": melhor_individuo.resposta, 
        "pontuacao": melhor_individuo.pontuacao,
        "individuo": melhor_individuo.id, 
        "Quantidade total gerada": total_individuos,
        "geracao": melhor_individuo.geracao,
        "Tempo Total": f"{(end-begin)/60} Minutos"
    }

    melhor_individuo.imprimir_resposta()
    # Salva o dicionário em um arquivo JSON
    with open(f'Melhor_Individuo_Torneio_{melhor_individuo.geracao}.json', 'w', encoding='utf-8') as f:
        json.dump(best_individuo_dict, f, indent=4, ensure_ascii=False)



path_json_individuo = R'Individuos\MELHOR_INDIVIDUO_14_ACERTOS.json'

show_individuo(path_json_individuo)

run_genetic()