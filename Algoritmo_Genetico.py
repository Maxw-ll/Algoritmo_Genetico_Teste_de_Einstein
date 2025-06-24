from Individuo import Individuo
import json
import Constantes


Population = [Individuo() for i in range(Constantes.QUANTIDADE_INDIVIDUOS)]


Population[0].imprimir_resposta()
print(Population[0].resposta)

for i in range(Constantes.QUANTIDADE_INDIVIDUOS):
    print(f"Individuo {i} Fitness: {Population[i].pontuacao}")
    if Population[i].pontuacao > 20:
        individuo = {
            "bits": ''.join(map(str, Population[i].cromossomos)), 
            "resposta": Population[i].resposta, 
            "pontuacao": Population[i].pontuacao,  
            "Individuo": i
        }

        # Salva o dicionário em um arquivo JSON
        with open(f'individuo_bom_{i}.json', 'w', encoding='utf-8') as f:
            json.dump(individuo, f, indent=4, ensure_ascii=False)
