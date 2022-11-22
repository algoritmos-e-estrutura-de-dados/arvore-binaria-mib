from node import Node

class BinaryTree:

    def __init__(self):
        self.root = None


    def adicionar(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node

        elif self.root.direita is None:
         self.root.direita = node
         self.root.setDireita
         

        elif self.root.esquerda is None:
         self.root.esquerda = node
         self.root.setEsquerda
         

    def esta_vazia(self):
        return (self.root == None)

    def __str__(self):
        return f'{self.root.direita} {self.root} {self.root.esquerda}' 

        


        



    


   
