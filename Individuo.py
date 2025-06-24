import numpy as np
import random

class Individuo():

    def __init__(self):
        self.quantidade_cromossomos: int = 75
        self.cromossomos: list = self.Aleatory_DNA()
        self.dictgenes: dict = {
            1: #Cores
            {
                '000': "Amarelo",
                '001': "Azul",
                '010': "Branco",
                '011': "Verde",
                '100': "Vermelho",
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
    

    def Aleatory_DNA(self) -> list:
        crs: list = []

        for i in range(self.quantidade_cromossomos):
            crs.append(random.randint(0,1))

        return crs
    

    def translate_to_string(self):
        print("-" * 75)
        print(f"{'CASA':<10} {'Cor':<10} {'Nacionalidade':<15} {'Bebida':<15} {'Cigarro':<15} {'Animal':<10}")
        print("-" * 75)

        for i in range(5):  # 5 casas
            atributos = []
            for j in range(5):  # 5 atributos por casa
                idx = (i * 5 + j) * 3
                bits = self.cromossomos[idx:idx + 3]
                chave_binaria = ''.join(map(str, bits))
                atributo = self.dictgenes[j + 1].get(chave_binaria, "Desconhecido")
                atributos.append(atributo)
            
            print(f"{'CASA #' + str(i+1):<10} {atributos[0]:<10} {atributos[1]:<15} {atributos[2]:<15} {atributos[3]:<15} {atributos[4]:<10}")




            
            




        
    