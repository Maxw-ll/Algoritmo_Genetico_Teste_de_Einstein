from Individuo import Individuo
import Constantes


Population = [Individuo() for i in range(Constantes.QUANTIDADE_INDIVIDUOS)]


Population[0].imprimir_resposta()

'''for i in range(5):
    print(f"{Population[0].cromossomos[i*15: i*15 + 15]}\n")'''