from __future__ import annotations
from collections.abc import Iterator

# O padrão Iterator fornece uma maneira de acessar os elementos de um objeto
# de coleção (como uma lista) sequencialmente, sem expor sua representação interna.

# --- A Forma Pythonic e Melhorada (Usando Geradores) ---
# Em Python, a maneira mais idiomática e simples de implementar o padrão Iterator
# é usando funções geradoras com a palavra-chave `yield`. Isso elimina a
# necessidade de criar uma classe de iterador separada, pois o Python
# gerencia o estado (como o índice atual) e a lógica de `__next__` e `StopIteration`
# automaticamente.

# --- 1. A Coleção (Aggregate) ---
class ListaDeProdutos:
    """
    A coleção de objetos que queremos percorrer.
    """
    def __init__(self, produtos: list[str] = None):
        self._produtos = produtos if produtos is not None else []

    def adicionar_produto(self, produto: str):
        self._produtos.append(produto)

    def __iter__(self) -> Iterator[str]:
        """
        Este é o método de fábrica do iterador padrão (forward).
        Usando `yield`, ele se torna um gerador, que é um tipo de iterador.
        """
        print("(Criando iterador forward)")
        for produto in self._produtos:
            yield produto

    def iterador_reverso(self) -> Iterator[str]:
        """
        Um método de fábrica para um iterador diferente (reverso).
        Também implementado como um gerador para simplicidade.
        """
        print("(Criando iterador reverso)")
        for produto in reversed(self._produtos):
            yield produto

# --- Código Cliente ---
# O cliente não precisa saber como a coleção é implementada.
# Ele só precisa saber que pode iterar sobre ela.

colecao = ListaDeProdutos()
colecao.adicionar_produto("Notebook Gamer")
colecao.adicionar_produto("Mouse sem fio")
colecao.adicionar_produto("Teclado Mecânico")

print("--- Iteração Padrão (Forward) ---")
# O `for` loop chama `__iter__` automaticamente para obter um iterador.
for item in colecao:
    print(f"Produto: {item}")

print("\n--- Iteração Reversa ---")
# Podemos usar o método de fábrica específico para obter um iterador diferente.
for item in colecao.iterador_reverso():
    print(f"Produto: {item}")

print("\n--- Múltiplas iterações independentes ---")
iterador1 = iter(colecao)
iterador2 = iter(colecao)

print(f"Iterador 1, item 1: {next(iterador1)}")
print(f"Iterador 2, item 1: {next(iterador2)}")
print(f"Iterador 1, item 2: {next(iterador1)}")
print(f"Iterador 2, item 2: {next(iterador2)}")

#Isso permite que a classe ListaDeProdutos seja usada diretamente em loops for, sem expor sua estrutura interna, tornando o código mais flexível e desacoplado.