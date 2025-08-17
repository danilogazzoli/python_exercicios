from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# O padrão Composite compõe objetos em estruturas de árvore para representar hierarquias
# parte-todo. Ele permite que os clientes tratem objetos individuais (folhas) e
# composições de objetos (composites) de maneira uniforme.

# --- 1. A Interface do Componente (Component) ---
# Declara a interface para objetos na composição, tanto para folhas quanto para composites.
class Componente(ABC):
    """
    A classe base Componente declara operações comuns para objetos
    simples e complexos de uma composição.
    """
    @abstractmethod
    def obter_tamanho(self):
        """Retorna o tamanho do componente."""
        pass

    @abstractmethod
    def mostrar(self, nivel: int = 0) -> None:
        """Exibe a estrutura do componente."""
        pass

    def adicionar(self, componente: Componente) -> None:
        """Por padrão, folhas não suportam adicionar componentes."""
        raise NotImplementedError("Este componente não suporta adicionar filhos.")

# --- 2. A Folha (Leaf) ---
# Representa os objetos finais de uma composição. Uma folha não pode ter filhos.
class Arquivo(Componente):
    """
    A classe Arquivo (Folha) representa os objetos finais de uma composição.
    """
    def __init__(self, nome: str, tamanho: int):
        self.nome = nome
        self.tamanho = tamanho

    def obter_tamanho(self):
        return self.tamanho

    def mostrar(self, nivel: int = 0) -> None:
        print(f"{'  ' * nivel}- Arquivo: {self.nome} ({self.tamanho} bytes)")

# --- 3. O Composite ---
# Define o comportamento para componentes que têm filhos.
# Armazena componentes filhos e implementa operações relacionadas a eles.
class Pasta(Componente):
    """
    A classe Pasta (Composite) contém componentes filhos (folhas ou outros composites).
    """
    def __init__(self, nome: str):
        self.nome = nome
        self._filhos: List[Componente] = []

    def adicionar(self, componente: Componente) -> None:
        self._filhos.append(componente)

    def obter_tamanho(self):
        return sum(filho.obter_tamanho() for filho in self._filhos)

    def mostrar(self, nivel: int = 0) -> None:
        print(f"{'  ' * nivel}+ Pasta: {self.nome}")
        for filho in self._filhos:
            filho.mostrar(nivel + 1)

# --- Código Cliente ---
pasta_raiz = Pasta("Raiz")
pasta_documentos = Pasta("Documentos")
pasta_imagens = Pasta("Imagens")

arquivo1 = Arquivo("doc1.txt", 100)
arquivo2 = Arquivo("img1.jpg", 500)

pasta_documentos.adicionar(arquivo1)
pasta_imagens.adicionar(arquivo2)

pasta_raiz.adicionar(pasta_documentos)
pasta_raiz.adicionar(pasta_imagens)

print("--- Estrutura de Arquivos ---")
pasta_raiz.mostrar()

print("\n--- Calculando Tamanhos ---")
print(f"Tamanho total da pasta '{pasta_raiz.nome}': {pasta_raiz.obter_tamanho()} bytes")
print(f"Tamanho total da pasta '{pasta_documentos.nome}': {pasta_documentos.obter_tamanho()} bytes")


# A classe Componente define uma interface comum com o método obter_tamanho, que é implementado tanto pela classe Arquivo quanto pela classe Pasta.
# A classe Arquivo retorna seu próprio tamanho, enquanto a classe Pasta calcula o tamanho total somando os tamanhos dos itens que contém, sejam arquivos ou outras pastas.
# Dessa forma, tanto arquivos quanto pastas podem ser tratados da mesma forma ao chamar obter_tamanho. O código cria uma estrutura de pastas e arquivos, adiciona os itens e, ao final, calcula o tamanho total da pasta raiz.