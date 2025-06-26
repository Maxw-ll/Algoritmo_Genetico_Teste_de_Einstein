import numpy as np
import random
import Constantes

class Individuo():

    def __init__(self, Cromossomos = None):
        self.quantidade_cromossomos: int = 75
        if Cromossomos != None:
            self.cromossomos = Cromossomos
        else:
            self.cromossomos: list = self.Aleatory_DNA()

        self.resposta: dict = self.translate_resposta()
        self.pontuacao: int = self.fitness()
        self.id = None
        self.geracao = 0

    
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
        
        self.translate_resposta()
        # Percorre os atributos e imprime os valores das casas como colunas
        for atributo in atributos:
            print(f"{atributo:<15} ", end="")  # Imprime o nome do atributo
            for i in range(1, 6):  # Para cada casa (de CASA #1 até CASA #5)
                casa_atributos = self.resposta[f'CASA {i}']
                print(f"{casa_atributos[atributo]:<16}", end="") 
            print()  

 
    def fitness(self):
        self.translate_resposta()
        score = 0  # Pontuação inicial
        
        # 1. O Norueguês vive na primeira casa.
        if self.resposta['CASA 1']['Nacionalidade'] == 'Norueguês':
            score += Constantes.PONTO_FACIL

        # 2. O Inglês vive na casa Vermelha.
        for casa, atributos in self.resposta.items():
            if atributos['Nacionalidade'] == 'Inglês' and atributos['Cor'] == 'Vermelha':
                score += Constantes.PONTO_MEDIA
                break

        # 3. O Sueco tem Cachorros como animais de estimação.
        for casa, atributos in self.resposta.items():
            if atributos['Nacionalidade'] == 'Sueco' and atributos['Animal'] == 'Cachorros':
                score += Constantes.PONTO_MEDIA
                break

        # 4. O Dinamarquês bebe Chá.
        for casa, atributos in self.resposta.items():
            if atributos['Nacionalidade'] == 'Dinamarquês' and atributos['Bebida'] == 'Chá':
                score += Constantes.PONTO_MEDIA
                break

        # 5. A casa Verde fica do lado esquerdo da casa Branca.
        for i in range(1, 5):  
            if self.resposta[f'CASA {i}']['Cor'] == 'Verde' and self.resposta[f'CASA {i+1}']['Cor'] == 'Branca':
                score += Constantes.PONTO_MEDIA
                break

        # 6. O homem que vive na casa Verde bebe Café.
        for casa, atributos in self.resposta.items():
            if atributos['Cor'] == 'Verde' and atributos['Bebida'] == 'Café':
                score += Constantes.PONTO_MEDIA
                break

        # 7. O homem que fuma Pall Mall cria Pássaros.
        for casa, atributos in self.resposta.items():
            if atributos['Cigarro'] == 'Pall Mall' and atributos['Animal'] == 'Pássaros':
                score += Constantes.PONTO_MEDIA
                break

        # 8. O homem que vive na casa Amarela fuma Dunhill.
        for casa, atributos in self.resposta.items():
            if atributos['Cor'] == 'Amarela' and atributos['Cigarro'] == 'Dunhill':
                score += Constantes.PONTO_MEDIA
                break

        # 9. O homem que vive na casa do meio bebe Leite.
        if self.resposta['CASA 3']['Bebida'] == 'Leite':
            score += Constantes.PONTO_FACIL

        # 10. O homem que fuma Blends vive ao lado do que tem Gatos.
        for i in range(1, 5):  
            if (self.resposta[f'CASA {i}']['Cigarro'] == 'Blends' and self.resposta[f'CASA {i+1}']['Animal'] == 'Gatos') or (self.resposta[f'CASA {i+1}']['Cigarro'] == 'Blends' and self.resposta[f'CASA {i}']['Animal'] == 'Gatos'):
                score += Constantes.PONTO_DIFICIL
                break

        # 11. O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        for i in range(1, 5):  
            if (self.resposta[f'CASA {i}']['Animal'] == 'Cavalos' and self.resposta[f'CASA {i+1}']['Cigarro'] == 'Dunhill') or (self.resposta[f'CASA {i+1}']['Animal'] == 'Cavalos' and self.resposta[f'CASA {i}']['Cigarro'] == 'Dunhill'):
                score += Constantes.PONTO_DIFICIL
                break

        # 12. O homem que fuma BlueMaster bebe Cerveja.
        for casa, atributos in self.resposta.items():
            if atributos['Cigarro'] == 'Blue Master' and atributos['Bebida'] == 'Cerveja':
                score += Constantes.PONTO_MEDIA
                break

        # 13. O Alemão fuma Prince.
        for casa, atributos in self.resposta.items():
            if atributos['Nacionalidade'] == 'Alemão' and atributos['Cigarro'] == 'Prince':
                score += Constantes.PONTO_MEDIA
                break

        # 14. O Norueguês vive ao lado da casa Azul.
        for i in range(1, 5):  
            if (self.resposta[f'CASA {i}']['Nacionalidade'] == 'Norueguês' and self.resposta[f'CASA {i+1}']['Cor'] == 'Azul') or (self.resposta[f'CASA {i+1}']['Nacionalidade'] == 'Norueguês' and self.resposta[f'CASA {i}']['Cor'] == 'Azul'):
                score += Constantes.PONTO_DIFICIL
                break

        # 15. O homem que fuma Blends é vizinho do que bebe Água.
        for i in range(1, 5):  
            if (self.resposta[f'CASA {i}']['Cigarro'] == 'Blends' and self.resposta[f'CASA {i+1}']['Bebida'] == 'Água') or (self.resposta[f'CASA {i+1}']['Cigarro'] == 'Blends' and self.resposta[f'CASA {i}']['Bebida'] == 'Água'):
                score += Constantes.PONTO_DIFICIL
                break

        #PUNIÇÃO SE TEM NONE  
        for casa, atributos in self.resposta.items():
            for atributo, valor in atributos.items():
                if valor == "None":
                    score -= Constantes.PONTO_PUNICAO
                    if score < 0:  # Não deixar a pontuação negativa
                        score = 0

        
        #PUNIÇÃO NOMES REPETIDOS
        for casa, atributos in self.resposta.items():
            contagem = {}
            for atributo, valor in atributos.items():
                if valor in contagem:
                    contagem[valor] += 1
                else:
                    contagem[valor] = 1
            # Se algum valor se repetir, subtrai pontos
            for valor, qtd in contagem.items():
                if qtd > 1 and valor != "None":  # Só conta repetição de valores não-None
                    score -= Constantes.PONTO_PUNICAO * qtd
                    if score < 0:  # Não deixar a pontuação negativa
                        score = 0

        self.pontuacao = score
        return score




        
    