import numpy as np
import random
import Constantes

class Individuo():

    def __init__(self):
        self.quantidade_cromossomos: int = 75
        self.cromossomos: list = self.Aleatory_DNA()
        self.resposta: dict = self.translate_resposta()

    
    def Aleatory_DNA(self) -> list:
        crs: list = []

        for i in range(self.quantidade_cromossomos):
            crs.append(random.randint(0,1))

        return crs
    
    def translate_resposta(self):

        resposta = {}

        for i in range(5):  # 5 casas
            casa_atributos = {}  # Dicionário de atributos para a casa atual
            
            for j in range(5):  # 5 atributos por casa
                idx = (i * 5 + j) * 3
                bits = self.cromossomos[idx:idx + 3]
                chave_binaria = ''.join(map(str, bits))
                atributo = Constantes.DICT_GENES[j + 1].get(chave_binaria, "Desconhecido")
                
                # Mapeia o atributo para o dicionário da casa
                if j == 0:
                    casa_atributos['Cor'] = atributo
                elif j == 1:
                    casa_atributos['Nacionalidade'] = atributo
                elif j == 2:
                    casa_atributos['Bebida'] = atributo
                elif j == 3:
                    casa_atributos['Cigarro'] = atributo
                elif j == 4:
                    casa_atributos['Animal'] = atributo
            
            # Adiciona a casa e seus atributos ao dicionário principal
            resposta[f'CASA {i+1}'] = casa_atributos
        
        return resposta
        

    def imprimir_resposta(self):
        print("-" * 100)
        print(f"{'Atributo':<15} {'CASA 1':<15} {'CASA 2':<15} {'CASA 3':<15} {'CASA 4':<15} {'CASA 5':<15}")
        print("-" * 100)
        
        # Listagem dos atributos que queremos imprimir nas linhas
        atributos = ['Cor', 'Nacionalidade', 'Bebida', 'Cigarro', 'Animal']
        
        # Percorre os atributos e imprime os valores das casas como colunas
        for atributo in atributos:
            print(f"{atributo:<15} ", end="")  # Imprime o nome do atributo
            for i in range(1, 6):  # Para cada casa (de CASA #1 até CASA #5)
                casa_atributos = self.resposta[f'CASA {i}']
                print(f"{casa_atributos[atributo]:<15}", end="") 
            print()  

    def calculate_fitness(self):
        pass 
            
            




        
    