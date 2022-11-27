from binary_tree import BinaryTree
import pyfiglet


#interface conjunto com while
ascii_banner = pyfiglet.figlet_format("Arvore binaria")
print(ascii_banner)


binary_tree = BinaryTree()

while (True):
    print("1 - Inserir um novo valor") #OK

    print("2 - Printar Pré-ordem") #OK

    print("3 - Printar Em-ordem") #OK

    print("4 - Printar Pós-ordem") #OK

    print("5 - Realizar busca") #OK
    #CORRIGIR BUSCA, ESTA SEMPRE RETORNANDO VALOR NAO ENCONTRADO, MESMO EXISTINDO
    #CORRIGIDO, PROBLEMA ERA DENTRO DO METODO RETURN DENTRO DA CLASSE BT > PERCORRE

    print("6 - Realizar remoção + Mostra árvore atualizada") #OK!
    #CORRIGIR PRINT DAS ATUALIZACOES NAO ESTA MOSTRANDO A BT
    #CORRIGIDO, REPLIQUEI OS PRINTS PRE,EM E POS DEU CERTO

    print("7 - Sair a execução") #OK


    operacao = input()

    if (operacao == "1"):
        value = input("Digite o valor a ser inserido: ")
        binary_tree.adicionar(int(value))

    elif (operacao == "2"):
        print("Arvore atual (Pré-Ordem): ")
        binary_tree.pre_ordem()
        pass

    elif (operacao == "3"):
        print("Arvore atual (Em-Ordem): ")
        binary_tree.em_ordem()
        pass    

    elif (operacao == "4"):
        print("Arvore atual (Pos-Ordem): ")
        binary_tree.pos_ordem()
        pass

    elif (operacao == "5"):
        value = int(input("Digite o valor a ser consultado: "))
        print("Valor encontrado" if binary_tree.procurar(value) else "Valor não encontrado")
        pass

    elif (operacao == "6"):
        value = int(input("Digite o valor a ser removido: "))
        print("Valor removido" if binary_tree.remover(value) else "Valor não removido, pois não existe na árvore")

        print("Arvore atualizada (Pré-Ordem): ")
        binary_tree.pre_ordem()
        print("Arvore atualizada (Em-Ordem): ")
        binary_tree.em_ordem()
        print("Arvore atualizada (Pós-Ordem): ")
        binary_tree.pos_ordem()
        pass

    elif (operacao == "7"):
        print("Execução finalizada")
        break

    else:
        print("Operação invalida")
        pass

