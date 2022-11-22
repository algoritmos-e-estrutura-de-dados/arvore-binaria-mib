
class Node:

    def __init__(self, value, direita = None, esquerda = None):
        self.value = value 
        self.direita = direita 
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def __str__(self):
        return f'{str(self.value)}' 


 



    
    
    