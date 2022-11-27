from node import Node
#BinaryTree contendo os métodos para adicionar e remover um nó. OK **FALTA REMOVER**
#Além disso, deve conter os métodos para percorrer também. OK
#Deve conter também um método para imprimir a arvore.


class BinaryTree:

#raiz
    def __init__(self):
        self.root = None

#ADICIONAR
    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            auxiliar = self.root
            while (True):
                if (auxiliar.value >= value):
                    ref_cima = auxiliar
                    auxiliar = auxiliar.get_esq()
                    ref_baixo = True

                else:
                    ref_cima = auxiliar
                    auxiliar = auxiliar.get_dir()
                    ref_baixo = False

                if (auxiliar is None):
                    break

            ref_cima.set_dir(node) if ref_baixo is False else ref_cima.set_esq(node)


#BUSCAR
    def procurar(self, busca: int):
        if self.root:
            return self.root.procurar(busca)
        else:
            return False


#REMOVER
    def remover(self, value: int):
        # valida arvore vazia
        if self.root is None:
            return False

        # valida arvore preenchida 
        elif self.root.value == value:
            if (self.root.get_dir() is None and self.root.get_dir() is None):
                self.root = None
            elif (self.root.get_esq() and self.root.get_dir() is None):
                self.root = self.root.get_esq()
            elif (self.root.get_esq() is None and self.root.get_dir()):
                self.root = self.root.get_dir()
            elif (self.root.get_esq() and self.root.get_dir()):

                #ref de cima
                aux_node_ref_topo = self.root       # aux vira nova ref_cima por sobrescrita
                remove_node: Node = self.root.get_dir()     #remove/sobrescreve na vdd

                while (remove_node.get_esq()):
                    aux_node_ref_topo = remove_node
                    remove_node = remove_node.get_esq()

                self.root.value = remove_node.value
                if remove_node.get_dir():
                    if aux_node_ref_topo.value > remove_node.value:
                        aux_node_ref_topo.set_esq(remove_node.get_dir())
                    elif aux_node_ref_topo.value < remove_node.value:
                        aux_node_ref_topo.set_dir(remove_node.get_dir())
                else:
                    if remove_node.value < aux_node_ref_topo.value:
                        aux_node_ref_topo.set_esq(None)
                    else:
                        aux_node_ref_topo.set_dir(None)
            return True

        #ref de baixo aux, settando novas posicoes
        new_ref_baixo = None    #nova ref para baixo/ realocar 
        node = self.root

        # laco para verificar do node ref_baixo 
        while node and node.value != value:
            new_ref_baixo = node
            if value < node.value:
                node = node.get_esq()
            elif value > node.value:
                node = node.get_dir()

        # verifica o resto da arvore parte de baixo se esta vazia
        if node is None or node.value != value:
            return False

        # setta os nos quando se nao tiver mais ref_baixo para ajeitar a arvore
        elif node.get_esq() is None and node.get_dir() is None:
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(None)
            else:
                new_ref_baixo.set_dir(None)
            return True

        # sobrescreve os nos ref baixo p baixo esquerda/realocando
        elif node.get_esq() and node.get_dir() is None:
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(node.get_esq())
            else:
                new_ref_baixo.set_dir(node.get_esq())
            return True

        # sobrescreve os nos ref baixo p baixo direita/realocando settando
        elif node.get_esq() is None and node.get_dir():
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(node.get_dir())
            else:
                new_ref_baixo.set_dir(node.get_dir())
            return True

         # sobrescreve os nos ref baixo p dois lados/realoca settando
        else:
            aux_node_ref_topo = node
            remove_node = node.get_dir()
            while remove_node.get_esq():
                aux_node_ref_topo = remove_node
                remove_node = remove_node.get_esq()
            node.value = remove_node.value
            if remove_node.get_dir():
                if aux_node_ref_topo.value > remove_node.value:
                    aux_node_ref_topo.set_esq(remove_node.get_dir())
                elif aux_node_ref_topo.value < remove_node.value:
                    aux_node_ref_topo.set_dir(remove_node.get_dir())
            else:
                if remove_node.value < aux_node_ref_topo.value:
                    aux_node_ref_topo.set_esq(None)
                else:
                    aux_node_ref_topo.set_dir(None)


#PERCORRIMENTOS
    def pre_ordem(self):
        if self.root is not None:
            self.root.pre_ordem()

    def em_ordem(self):
        if self.root is not None:
            self.root.em_ordem()

    def pos_ordem(self):
        if self.root is not None:
            self.root.pos_ordem()

    def print_bt(self):
        print("Arvore atualizada (Pré-Ordem): ")
        print(self.pre_ordem())
        print("Arvore atualizada (Em-Ordem): ")
        print(self.em_ordem())
        print("Arvore atualizada (Pós-Ordem): ")
        print(self.pos_ordem())