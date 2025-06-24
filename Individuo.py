import numpy as np
import random
import Constantes

class Individuo():

    def __init__(self):
        self.quantidade_cromossomos: int = 75
        self.cromossomos: list = self.Aleatory_DNA()

    
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
                atributo = Constantes.DICT_GENES[j + 1].get(chave_binaria, "Desconhecido")
                atributos.append(atributo)
            
            print(f"{'CASA #' + str(i+1):<10} {atributos[0]:<10} {atributos[1]:<15} {atributos[2]:<15} {atributos[3]:<15} {atributos[4]:<10}")

    def calculate_fitness(self):
        pass 
            
            




        
    