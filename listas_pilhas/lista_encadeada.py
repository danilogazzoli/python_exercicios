'''
 No último elemento da lista, o apontador para o próximo possui um desenho diferente, 
 indicando que ele não aponta para nenhum elemento, ou seja, seu ponteiro proximo é None.

 
 TRADEOFFS:

 - inserção rápida
 - gasta menos memória RAM na criação
 - mais lenta na remoção dos elementos no fim
 - anda somente em um sentido (a partir da cabeça), não consegue retornar
 '''

class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)

        # 2) Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = self.cabeca

        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        self.cabeca = novo_nodo


    def insere_depois(self, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)

        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo

        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo

    def busca(self, valor):
        corrente = self.cabeca
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        return corrente, anterior
    
    def remove(self, valor):
        assert self.cabeca, "Impossível remover valor de lista vazia."

        # Nodo a ser removido é a cabeça da lista.
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            # Encontra a posição do elemento a ser removido.
            corrente, anterior = self.busca(valor)
            # O nodo corrente é o nodo a ser removido.
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                raise Exception('nó não encontrado')


if __name__ =='__main__':
    lista = ListaEncadeada()
    print("Lista vazia:", lista)

    lista.insere_no_inicio( 5)
    print("Lista contém um único elemento:", lista)

    lista.insere_no_inicio( 10)
    print("Inserindo um novo elemento:", lista)


    nodo_anterior = lista.cabeca
    lista.insere_depois(nodo_anterior, 20)
    print("Inserindo um novo elemento depois de um outro:", lista)


    lista.remove(5)
    print(lista)

    lista.remove(10)
    print(lista)

    lista.remove(20)
    print(lista)
