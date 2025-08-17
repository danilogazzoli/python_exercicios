# -*- coding: utf-8 -*-

"""
Lista Circular Encadeada

Uma lista circular é uma variação da lista encadeada em que o último elemento
aponta de volta para o primeiro, em vez de apontar para None. Isso cria um ciclo.

TRADEOFFS:
 - Útil para estruturas de dados que precisam de um comportamento de "rodízio",
   como um buffer circular ou um carrossel.
 - Qualquer nó pode ser um ponto de partida para a travessia.
 - A travessia deve ter cuidado para não entrar em um loop infinito. É preciso
   verificar se já voltamos ao nó inicial.
"""

class Node:
    """Representa um nó na lista circular."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Implementação de uma Lista Circular Encadeada."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adiciona um nó ao final da lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Aponta para si mesmo
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        """Adiciona um nó no início da lista."""
        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            # Encontra o último nó para atualizar seu ponteiro 'next'
            while current.next != self.head:
                current = current.next
            current.next = new_node
        
        self.head = new_node

    def remove(self, key):
        """Remove um nó da lista pelo seu valor (key)."""
        if not self.head:
            print("Erro: A lista está vazia.")
            return

        # Caso 1: O nó a ser removido é a cabeça (head)
        if self.head.data == key:
            current = self.head
            # Encontra o último nó
            while current.next != self.head:
                current = current.next
            
            if self.head == self.head.next:  # Se for o único nó
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        # Caso 2: O nó está em outra posição
        current = self.head
        prev = None
        while True:
            if current.data == key:
                prev.next = current.next
                return
            
            prev = current
            current = current.next
            
            # Se voltamos ao início, o nó não foi encontrado
            if current == self.head:
                print(f"Erro: O valor '{key}' não foi encontrado na lista.")
                break

    def print_list(self):
        """Exibe todos os nós da lista de forma segura."""
        if not self.head:
            print("Lista vazia.")
            return

        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(nodes) + " -> (volta para a cabeça)")


if __name__ == '__main__':
    clist = CircularLinkedList()
    print("--- Adicionando elementos ---")
    clist.append("A")
    clist.append("B")
    clist.prepend("C")
    clist.append("D")
    clist.print_list()  # Saída: C -> A -> B -> D -> (volta para a cabeça)

    print("\n--- Removendo elementos ---")
    clist.remove("B")
    print("Após remover 'B':")
    clist.print_list()

    clist.remove("C")
    print("Após remover 'C' (a cabeça):")
    clist.print_list()

    clist.remove("X") # Tentando remover um item que não existe