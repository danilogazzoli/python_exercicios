# -*- coding: utf-8 -*-


'''
 TRADEOFFS:

 - começa por qualquer lado
 - gasta mais memória
 - costuma ter melhor performance
 - possui as referências de ida e volta, ao percorrer a lista, pode-se avançar ou retornar os objetos
 
'''

class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class ListaDuplamenteLigada:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio
    
    @property
    def fim(self):
        return self._fim
    
    @property
    def quantidade(self):
        return self._quantidade

    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def inserir_no_inicio(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.proximo = self.inicio
        self._inicio.anterior = celula
        self._inicio = celula
        self._quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.anterior = self.fim
        self.fim.proximo = celula
        self._fim = celula
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            return self.inserir_no_inicio(conteudo)
        if posicao == self.quantidade:
            return self.inserir_no_fim(conteudo)
        esquerda = self._celula(posicao-1)
        direita = esquerda.proximo
        celula = Celula(conteudo)
        celula.proximo = direita
        celula.anterior = esquerda
        esquerda.proximo = celula
        direita.anterior = celula
        self._quantidade += 1

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida: {}".format(posicao))

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        metade = self.quantidade // 2
        if posicao < metade:
            atual = self.inicio
            for i in range(0, posicao):
                atual = atual.proximo
            return atual
        atual = self.fim
        for i in range(posicao+1, self.quantidade)[::-1]:
            atual = atual.anterior
        return atual

    def _remover_ultimo(self):
        if self.quantidade == 1:
            removido = self.inicio
            self._inicio = None
            self._fim = None
            self._quantidade -= 1
            return removido.conteudo

    def remover_do_inicio(self):
        if self.quantidade == 1:
            return self._remover_ultimo()
        removido = self.inicio
        self._inicio = removido.proximo
        self._inicio.anterior = None
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover_do_fim(self):
        if self.quantidade == 1:
            return self._remover_ultimo()
        removido = self.fim
        self._fim = removido.anterior
        self._fim.proximo = None
        removido.anterior = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_do_inicio()
        if posicao == self.quantidade - 1:
            return self.remover_do_fim()
        removido = self._celula(posicao)
        esquerda = removido.anterior
        direita = removido.proximo
        removido.proximo = None
        removido.anterior = None
        esquerda.proximo = direita
        direita.anterior = esquerda
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo


class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return " * {} - {}".format(self.nome, self.endereco)


def situacao(lista):
    print("Quantidade: {}".format(lista.quantidade))
    lista.imprimir()


def main():
    loja1 = Loja("Minimercardo", "Rua das Flores, 12")
    loja2 = Loja("Hortifruti", "Av das Borboletas, 23")
    loja3 = Loja("Padaria Pão Quente", "Praça da Árvore")
    loja4 = Loja("Supermercado", "Rua do Pomar, 23")
    loja5 = Loja("Mercado", "Rua das Flores, 98")
    loja6 = Loja("Quitanda", "Rua da Fazenda, 899")
    loja7 = Loja("Minimercardo das Frutas", "Av do Bosque, 66")
    loja8 = Loja("Supermercado das Frutas", "Rua do Pomar, 600")
    loja9 = Loja("Hortifruti da terra", "Rua das Laranjeira, 800")
    loja10 = Loja("Mercado do Campo", "Rua da Fazenda, 1500")

    lista = ListaDuplamenteLigada()
    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)
    lista.inserir_no_fim(loja4)
    lista.inserir_no_fim(loja5)
    lista.inserir_no_fim(loja6)
    lista.inserir(2, loja7)
    lista.inserir(7, loja8)
    lista.inserir(0, loja9)
    lista.inserir(6, loja10)
    situacao(lista)

    removido = lista.remover_do_inicio()
    print("Removido do início: {}".format(removido))
    situacao(lista)

    removido = lista.remover_do_fim()
    print("Removido do fim: {}".format(removido))
    situacao(lista)

    removido = lista.remover(1)
    print("Removido da posição 1: {}".format(removido))
    situacao(lista)

    removido = lista.remover(5)
    print("Removido da posição 5: {}".format(removido))
    situacao(lista)

    removido = lista.remover(0)
    print("Removido da posição 0: {}".format(removido))
    situacao(lista)

    removido = lista.remover(4)
    print("Removido da posição 4: {}".format(removido))
    situacao(lista)


if __name__ == '__main__': 
    main()