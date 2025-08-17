from __future__ import annotations
from abc import ABC, abstractmethod
import copy

# O padrão Prototype permite criar novos objetos copiando um objeto existente (um "protótipo"),
# em vez de criar o objeto do zero. É útil quando o custo de criar um objeto
# é mais caro do que copiá-lo.

# --- 1. A Interface do Prototype ---
# Define a interface de clonagem.
class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Prototype:
        pass

# --- 2. O Protótipo Concreto ---
# A classe que implementa o método de clonagem.
class Produto(Prototype):
    def __init__(self, nome: str, material: str, cor: str, preco: float, componentes: list = None):
        self.nome = nome
        self.material = material
        self.cor = cor
        self.preco = preco
        # Usamos uma lista para demonstrar a importância do deepcopy
        self.componentes = componentes if componentes is not None else []

    def clone(self) -> Produto:
        """
        Cria uma cópia profunda do objeto. `deepcopy` é crucial para que
        objetos aninhados (como a lista de componentes) também sejam copiados,
        evitando que o clone e o original compartilhem referências.
        """
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (f"Produto: {self.nome} ({self.material}, {self.cor}) - "
                f"R${self.preco:.2f} - Componentes: {self.componentes}")

# --- 3. Registro de Protótipos (Opcional, mas recomendado) ---
# Centraliza o acesso aos protótipos, desacoplando ainda mais o cliente.
class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def add_prototype(self, name: str, prototype: Prototype):
        self._prototypes[name] = prototype

    def get_clone(self, name: str) -> Prototype:
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"Protótipo '{name}' não encontrado no registro.")
        return prototype.clone()

# --- Código Cliente ---

# 1. Configuração: Criar e registrar os protótipos iniciais.
registry = PrototypeRegistry()

cadeira_prototipo = Produto(
    nome="Cadeira Padrão", material="Madeira", cor="Branca", preco=150.00,
    componentes=["assento", "encosto", "4 pernas"]
)
registry.add_prototype("cadeira_madeira", cadeira_prototipo)

# 2. Uso: O cliente pede clones ao registro e os personaliza.
print("--- Criando objetos a partir de protótipos registrados ---")

cadeira_luxo = registry.get_clone("cadeira_madeira")
cadeira_luxo.nome = "Cadeira de Luxo"
cadeira_luxo.cor = "Marrom Escuro"
cadeira_luxo.preco = 250.00
print(f"Clone 1: {cadeira_luxo}")

banqueta = registry.get_clone("cadeira_madeira")
banqueta.nome = "Banqueta de Cozinha"
banqueta.preco = 120.00
banqueta.componentes[-1] = "base única de metal" # Modificando um componente aninhado
print(f"Clone 2: {banqueta}")

# 3. Verificação: O protótipo original permanece intacto.
print("\n--- Verificando o protótipo original ---")
print(f"Original: {cadeira_prototipo}")

'''
O método clonar permite gerar novos produtos com características similares, mas com modificações específicas, como mudanças no nome, cor ou preço, sem precisar recriar todos os atributos do zero.
'''