from Individuo import Individuo


QUANTIDADE_INDIVIDUOS = 40

Population = [Individuo() for i in range(QUANTIDADE_INDIVIDUOS)]


Population[0].translate_to_string()

'''for i in range(QUANTIDADE_INDIVIDUOS):
    print(Population[i].cromossomos)'''