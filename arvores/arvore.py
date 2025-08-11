'''
binária = 0, 1 ou 2 nós
estritamente binária = 0 ou 2 nós
árvore avl = árvore balanceada B, B+
 - árvore binária de busca, percursos: ordem, pré ordem, pós ordem
 - movimento de rotação 
folhas = nós terminais, que não tem filhos
grau = número de filhos em uma árvore
profundidade = distância do nó folha até a raiz
'''

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)
    
    def em_ordem(raiz):
        if not raiz:
            return

        # Visita filho da esquerda.
        em_ordem(raiz.esquerda)

        # Visita nodo corrente.
        print(raiz.chave),

        # Visita filho da direita.
        em_ordem(raiz.direita)
