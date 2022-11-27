class Node:
#O arquivo node.py deve conter a classe Node. 


#MÉTODO CRIA NODE
    def __init__(self, value, direita=None, esquerda=None):
        self.value = value
        self.direita = direita
        self.esquerda = esquerda

#MÉTODOS SET E GET REFERENCIA DO NÓ
    def set_dir(self, direita):
        self.direita = direita

    def set_esq(self, esquerda):
        self.esquerda = esquerda


    def get_esq(self):
        return self.esquerda

    def get_dir(self):
        return self.direita


#MÉTODOS PARA PROCURAR REFERENCIA NOD
    def procurar(self, busca: int):
        if (self.value == busca):
            return True

        elif self.value > busca:
            if self.esquerda:
                return self.esquerda.procurar(busca)
            else:
                return False

        else:
            if self.direita:
                return self.direita.procurar(busca)
            else:
                return False


#PERCURSOS REF NOD
    def pre_ordem(self):
        if self:
            print(str(self.value))
            if self.esquerda:
                self.esquerda.pre_ordem()
            if self.direita:
                self.direita.pre_ordem()
    
    def em_ordem(self):
        if self:
            if self.esquerda:
                self.esquerda.em_ordem()
            print (str(self.value))
            if self.direita:
                self.direita.em_ordem()

    def pos_ordem(self):
        if self:
            if self.esquerda:
                self.esquerda.pos_ordem()
            if self.direita:
                self.direita.pos_ordem()
            print (str(self.value))


