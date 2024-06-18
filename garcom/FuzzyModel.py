# Sistema de inferencia fuzzy para o problema da gorjeta

from simpful import *
import json

class FuzzyModelGorjeta():
    def __init__(self):
        # Criacao do sistema de inferencia fuzzy
        self.FS = FuzzySystem(verbose=False)

        # Definicao das entradas
        ## entrada Servico
        S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=3), term="ruim") # saida = [0% 100% 0%]
        S_2 = FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="bom")
        S_3 = FuzzySet(function=Triangular_MF(a=5, b=10, c=10), term="excelente")
        self.FS.add_linguistic_variable("Servico", 
                                LinguisticVariable([S_1, S_2, S_3], 
                                                    concept="Qualidade do servico", 
                                                    universe_of_discourse=[0, 10]))

        ## entrada comida
        F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="ruim")
        F_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=10), term="boa")
        self.FS.add_linguistic_variable("Comida", 
                                LinguisticVariable([F_1, F_2], 
                                                    concept="Qualidade da comida", 
                                                    universe_of_discourse=[0,10]))

        # Definicao da sauda
        ## Saida gorjeta
        T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="pequena")
        T_2 = FuzzySet(function=Triangular_MF(a=0, b=12.5, c=25), term="media")
        T_3 = FuzzySet(function=Triangular_MF(a=12.5, b=25, c=25), term="generosa") 
        self.FS.add_linguistic_variable("Gorjeta", 
                                LinguisticVariable([T_1, T_2, T_3], 
                                                    universe_of_discourse=[0,25]))

        #Definicao das regras do sistema
        R1 = "IF (Servico IS ruim) AND (Comida IS ruim) THEN (Gorjeta IS pequena)"
        R2 = "IF (Servico IS ruim) AND (Comida IS boa) THEN (Gorjeta IS media)"
        R3 = "IF (Servico IS bom) AND (Comida IS ruim) THEN (Gorjeta IS media)"
        R4 = "IF (Servico IS bom) AND (Comida IS boa) THEN (Gorjeta IS generosa)"
        R5 = "IF (Servico IS excelente) THEN (Gorjeta IS generosa)"
        self.FS.add_rules([R1, R2, R3, R4, R5])

    def model_predict(self, servico, comida):

        # Configurando as entradas
        self.FS.set_variable("Servico", servico)
        self.FS.set_variable("Comida", comida)

        # Obtendo a resposta
        resposta = dict()
        resposta['comida'] = comida
        resposta['servico'] = servico
        resposta['gorjeta'] = self.FS.Mamdani_inference(["Gorjeta"])["Gorjeta"]
        
        return json.dumps(resposta)