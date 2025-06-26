#PARÂMETROS ALGORITMO
QUANTIDADE_INDIVIDUOS = 5000
PONTUACAO_MAXIMA = 32
LIMITE_ACEITAVEL = 32
TAXA_MUTACAO = 0.070
TAXA_CROSSOVER = 0.75
NUM_GERACOES = 2000
QUANTIDADE_CORTE_MELHORES = 100

#PONTUAÇÃO REGRAS
PONTO_FACIL = 1
PONTO_MEDIA = 2
PONTO_DIFICIL = 3
PONTO_PUNICAO = 3


#DICIONÁRIO DE GENES
DICT_GENES: dict = {
    1: #Cores
    {
        '000': "Amarela",
        '001': "Azul",
        '010': "Branca",
        '011': "Verde",
        '100': "Vermelha",
        '101': "None",
        '110': "None",
        '111': "None"
    },
    2: #Nacionalidades
    {
        '000': "Alemão",
        '001': "Dinamarquês",
        '010': "Inglês",
        '011': "Norueguês",
        '100': "Sueco",
        '101': "None",
        '110': "None",
        '111': "None"
    },
    3: # Bebida
    {
        '000': "Água",
        '001': "Café",
        '010': "Chá",
        '011': "Cerveja",
        '100': "Leite",
        '101': "None",
        '110': "None",
        '111': "None"
    },
    4: #Cigarro
    {
        '000': "Blends",
        '001': "Blue Master",
        '010': "Dunhill",
        '011': "Pall Mall",
        '100': "Prince",
        '101': "None",
        '110': "None",
        '111': "None"
    },
    5: #Animal
    {
        '000': "Cachorros",
        '001': "Cavalos",
        '010': "Gatos",
        '011': "Pássaros",
        '100': "Peixes",
        '101': "None",
        '110': "None",
        '111': "None"
    }
}