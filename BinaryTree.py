'''
Classe para instanciação de nós que vão ficar na memória
'''

class Node:
    def __init__(self,data:object):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        self.__rightChild = newRightChild

    def insertLeft(self, data:object):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data:object):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self)->bool:
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        return self.__rightChild != None
        
	    
'''
Classe para a instanciação de Árvores Binárias
Autor: Alex Sandro
Data da última modificação: 11/05/2022
'''
class BinaryTree:
    # constructor that initializes an empty Tree 
    def __init__(self, data_root:object):
        self.__root = Node(data_root)
        # O cursor é um apontador usado para navegar na árvore (sem mexer no root)
        self.__cursor = self.__root

    def getRoot(self)->'Node':
        '''Obtem a referência para o nó "root"'''
        return self.__root

    def getCursor(self)->'Node':
        '''Obtem a referência para o nó apontado pelo "cursor"'''
        return self.__cursor

    def downLeft(self)->'Node':
        '''Desloca para o filho a esquerda do nó "cursor"
           Se não tiver filho, retorna None'''
        if(self.__cursor.hasLeftChild()): 
            self.__cursor = self.__cursor.leftChild
            return self.__cursor
        else:
            return None
            
    def downRight(self)->'Node':
        '''Desloca para o filho à direita do nó "cursor"
           Se não tiver filho, retorna None'''        
        if(self.__cursor.hasRightChild()): 
            self.__cursor = self.__cursor.rightChild
            return self.__cursor
        else:
            return None

    def addLeftChild(self, dado:object):
        '''Adiciona um filho à esquerda do nó apontado pelo "cursor"
           Se cursor já tiver filho esquerdo, não faz nada.'''
        if(not self.__cursor.hasLeftChild()):
            self.__cursor.leftChild = Node(dado)
            self.downLeft()
            

    def addRightChild(self, dado:object):
        '''Adiciona um filho à direita do nó apontado pelo "cursor"
           Se cursor já tiver filho direito, não faz nada.'''
        if(not self.__cursor.hasRightChild()):
            self.__cursor.rightChild = Node(dado)
            self.downRight()

    def resetCursor(self):
        '''Posiciona o cursor para o nó raiz'''
        self.__cursor = self.__root


    def search(self, chave:object )->Node:
        '''Realiza uma busca na árvore pelo nó cuja carga é igual à chave
           passada como argumento.
           Returns
           ---------
           True: caso a chave seja encontrada na árvore
           False: caso a chave não esteja na árvore
        '''
        return self.__searchData(chave, self.__root)
    
    def __searchData(self, chave, node):
        if (node == None):
            return None # Nao encontrou a chave
        if ( chave == node.data):
            return node
        elif ( self.__searchData( chave, node.leftChild)):
            return  self.__searchData( chave, node.leftChild)
        else:
            return self.__searchData( chave, node.rightChild)

    def preorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pré-ordem'''
        self.__preorder(self.__root)

    def inorderTraversal(self):
        '''Exibe os nós da árvore com percurso em in-ordem'''
        self.__inorder(self.__root)

    def postorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pós-ordem'''
        self.__postorder(self.__root)
        
    def __preorder(self, node):
        if( node == None):
            return
        print(f'{node.data} ',end='')
        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node == None):
            return
        self.__inorder(node.leftChild)
        print(f'{node.data} ',end='')
        self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node == None):
            return
        self.__postorder(node.leftChild)
        self.__postorder(node.rightChild)
        print(f'{node.data} ',end='')

    def deleteTree(self):
        '''Elimina todos os nós da árvore'''
        # garbage collector fará o trabalho de eliminação dos nós
        # abandonados 
        self.__root = None

    # o cursor tem que estar posicionado no nó pai
    # do nó que vai ser removido
    def deleteNode(self, key:object):
        '''Remove o nó determinado pela chave de busca.
           IMPORTANTE:
           a) o cursor deve estar posicionado no nó pai ao nó chave.
           b) se não puder ser removido (árvore vazia, cursor no local errado,...)
              não é executada qualquer ação'''
        self.__deleteNode(self.__cursor, key)


    def __deleteNode(self,root, key):

        if root is None: 
            return
        elif root.leftChild == None and root.rightChild == None:
            return
        
        if root.leftChild == None:
            if root.rightChild.data == key:
                root.rightChild = None
        elif root.rightChild == None:
            if root.leftChild.data == key:
                root.leftChild = None


if __name__ == '__main__':  
    arq = open('entrada.txt','r')
    arquivo = arq.readlines()
    listaDeArvores = []

    for dominio in arquivo:
        dominio = dominio.lower()
        listaDominio = dominio.split('/')
        # print(listaDominio)
        # o .strip() remove o \n
        dominioRaiz = listaDominio[0].strip()

        arvoreQueJaExiste = None

        # Aqui vamos pesquisar se ja existe uma arvore na listaDeArvores para o dominioRaiz
        for arvoreDaLista in listaDeArvores:
            if arvoreDaLista.getRoot().data == dominioRaiz:
                arvoreQueJaExiste = arvoreDaLista
                # se eh igual quer dizer que ja existe uma arvore para esse dominioRaiz

        if arvoreQueJaExiste == None:
            # cria uma nova arvore
            novaArvore = BinaryTree(dominioRaiz)
            listaDeArvores.append(novaArvore)
            arvoreQueJaExiste = novaArvore

        arvoreQueJaExiste.resetCursor()
        
        # usar o listaDominio para inserir os novos filhos
        for filho in listaDominio[1:]:
            filho = filho.strip()
            noFilho = arvoreQueJaExiste.search(filho)
            if noFilho == None:
                # nao achou o filho, tem que inserir
                if arvoreQueJaExiste.getCursor().hasLeftChild() == False:
                    # posso botar na esquerda
                    arvoreQueJaExiste.addLeftChild(filho)
                else:
                    arvoreQueJaExiste.addRightChild(filho)
                    # preciso  botar na direita
            elif arvoreQueJaExiste.getCursor().leftChild.data == filho:
                arvoreQueJaExiste.downLeft()
            else:
                arvoreQueJaExiste.downRight()
                
    for arvore in listaDeArvores:
        arvore.preorderTraversal()
        print()


    while True:

        urlBuscada = input('Digite a URL de pesquisa ou #sair para encerrar o programa:').lower()
        listaDaUrlBuscada = urlBuscada.split("/")
        dominioRaiz = listaDaUrlBuscada[0]

        achei = True
        arvoreAserBuscada = None

        for arvore in listaDeArvores:
            arvore.resetCursor()
            raiz = arvore.getRoot()
            if raiz.data == dominioRaiz:
                arvoreAserBuscada = arvore

        if arvoreAserBuscada == None:
            print('DEU RUIM')
            continue
        


        for filho in listaDaUrlBuscada[1:]:
            if arvoreAserBuscada.getCursor().leftChild.data == filho:
                arvoreAserBuscada.downLeft()

            elif arvoreAserBuscada.getCursor().rightChild.data == filho:
                arvoreAserBuscada.downRight()

            else:
                achei = False

        if achei:
            print('DEU CERTO')
        else:
            print('DEU RUIM')
