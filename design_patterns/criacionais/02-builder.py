# BUILDER = LINHA DE MONTAGEM

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# O padrão Builder separa a construção de um objeto complexo de sua representação,
# permitindo que o mesmo processo de construção possa criar diferentes representações.

# --- 1. Product ---
# O objeto complexo que queremos construir.
class Computador:
    def __init__(self):
        self.partes = {}

    def adicionar(self, parte: str, valor: Any):
        self.partes[parte] = valor

    def __str__(self):
        if not self.partes:
            return "Computador vazio."
        config = ", ".join(f"{chave}: {valor}" for chave, valor in self.partes.items())
        return f"Configuração do Computador: {config}"

# --- 2. Abstract Builder ---
# A interface Builder especifica métodos para criar as diferentes partes do objeto Product.
class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> Computador:
        pass

    @abstractmethod
    def set_cpu(self, cpu: str) -> IBuilder:
        pass

    @abstractmethod
    def set_memoria(self, memoria: int) -> IBuilder:
        pass

    @abstractmethod
    def set_armazenamento(self, armazenamento: str) -> IBuilder:
        pass

# --- 3. Concrete Builder ---
# Implementa a interface Builder e fornece uma maneira de recuperar o produto.
# O Builder concreto é responsável por criar e montar o produto.
class ComputadorBuilder:
    def __init__(self):
        """
        Um builder concreto deve ter um objeto produto que ele constrói.
        Começamos com um produto em branco que é montado passo a passo.
        """
        self.reset()

    def reset(self):
        self._product = Computador()

    @property
    def product(self) -> Computador:
        """
        O resultado final é recuperado aqui. É uma boa prática que o builder
        seja resetado após retornar o produto, para que esteja pronto para
        construir um novo produto.
        """
        produto_final = self._product
        self.reset()
        return produto_final

    def set_cpu(self, cpu: str) -> ComputadorBuilder:
        self._product.adicionar("CPU", cpu)
        return self

    def set_memoria(self, memoria: int) -> ComputadorBuilder:
        self._product.adicionar("Memória", f"{memoria}GB")
        return self

    def set_armazenamento(self, armazenamento: str) -> ComputadorBuilder:
        self._product.adicionar("Armazenamento", armazenamento)
        return self

# --- 4. Director (Opcional) ---
# O Diretor é responsável por executar os passos de construção em uma sequência particular.
# É útil se você tem "receitas" de construção complexas e recorrentes.
class Diretor:
    def __init__(self, builder: IBuilder):
        self._builder = builder

    def construir_pc_gamer(self):
        self._builder.set_cpu("Intel i9").set_memoria(32).set_armazenamento("2TB NVMe SSD")

    def construir_pc_escritorio(self):
        self._builder.set_cpu("Intel i5").set_memoria(16).set_armazenamento("512GB SATA SSD")

# --- Client Code ---
print("--- Construção manual com o Builder ---")
builder = ComputadorBuilder()

pc_personalizado = builder.set_cpu("AMD Ryzen 7").set_memoria(64).product
print(f"PC Personalizado: {pc_personalizado}")

print("\n--- Construção com o Diretor ---")
builder_para_diretor = ComputadorBuilder()
diretor = Diretor(builder_para_diretor)

diretor.construir_pc_gamer()
pc_gamer = builder_para_diretor.product
print(f"PC Gamer (via Diretor): {pc_gamer}")

diretor.construir_pc_escritorio()
pc_escritorio = builder_para_diretor.product
print(f"PC de Escritório (via Diretor): {pc_escritorio}")


#Uma interface Builder abstrata: Define o contrato para todos os builders.
#Um Builder concreto: Implementa o contrato e, crucialmente, cria um novo produto a cada vez.
#Um Diretor (opcional, mas recomendado): Uma classe que sabe a "receita" para construir configurações específicas (como "PC Gamer" ou "PC de Escritório"), utilizando um builder. Isso separa o o quê construir do como construir.

############   OUTRO EXEMPLO:

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

# --- 1. O Produto ---
# O objeto complexo que estamos construindo. Neste caso, um Bolo.
class Bolo:
    def __init__(self):
        self.massa = None
        self.recheio = None
        self.cobertura = None
        self.extras: List[str] = []

    def __str__(self) -> str:
        receita = [
            f"Bolo com massa de {self.massa or 'indefinida'}",
            f"Recheio de {self.recheio or 'nenhum'}",
            f"Cobertura de {self.cobertura or 'nenhuma'}",
        ]
        if self.extras:
            receita.append(f"Extras: {', '.join(self.extras)}")
        
        return ". ".join(receita) + "."

# --- 2. A Interface do Builder (Abstrato) ---
# Define os passos de construção que todos os builders de bolo devem ter.
class IBoloBuilder(ABC):
    @property
    @abstractmethod
    def produto(self) -> Bolo:
        pass

    @abstractmethod
    def definir_massa(self, tipo: str) -> IBoloBuilder:
        pass

    @abstractmethod
    def definir_recheio(self, tipo: str) -> IBoloBuilder:
        pass

    @abstractmethod
    def definir_cobertura(self, tipo: str) -> IBoloBuilder:
        pass
    
    @abstractmethod
    def adicionar_extra(self, extra: str) -> IBoloBuilder:
        pass

# --- 3. O Builder Concreto ---
# Implementa a interface e gerencia a criação do objeto Bolo.
class BoloBuilder(IBoloBuilder):
    def __init__(self):
        """Inicia o builder com um produto vazio que será montado."""
        self.reset()

    def reset(self):
        """Reseta o builder para começar a construção de um novo bolo."""
        self._produto = Bolo()

    @property
    def produto(self) -> Bolo:
        """Retorna o bolo construído e reseta o builder para o próximo uso."""
        bolo_final = self._produto
        self.reset()
        return bolo_final

    def definir_massa(self, tipo: str) -> BoloBuilder:
        self._produto.massa = tipo
        return self

    def definir_recheio(self, tipo: str) -> BoloBuilder:
        self._produto.recheio = tipo
        return self

    def definir_cobertura(self, tipo: str) -> BoloBuilder:
        self._produto.cobertura = tipo
        return self
        
    def adicionar_extra(self, extra: str) -> BoloBuilder:
        self._produto.extras.append(extra)
        return self

# --- 4. O Diretor (Opcional) ---
# O Confeiteiro conhece as "receitas" e usa o builder para montar bolos específicos.
class Confeiteiro:
    def __init__(self, builder: IBoloBuilder):
        self._builder = builder

    def fazer_bolo_floresta_negra(self):
        """Uma receita específica: Bolo Floresta Negra."""
        self._builder.definir_massa("Chocolate") \
                     .definir_recheio("Cereja e Chantilly") \
                     .definir_cobertura("Raspas de Chocolate") \
                     .adicionar_extra("Cerejas no topo")

    def fazer_bolo_de_festa(self):
        """Outra receita: Bolo de Festa."""
        self._builder.definir_massa("Baunilha") \
                     .definir_recheio("Doce de Leite") \
                     .definir_cobertura("Chantininho") \
                     .adicionar_extra("Granulados coloridos")

# --- Código Cliente ---

# 1. Construção manual, passo a passo (ótimo para bolos personalizados)
print("--- Construindo um bolo personalizado ---")
builder = BoloBuilder()

bolo_personalizado = (
    builder.definir_massa("Laranja")
           .definir_cobertura("Ganache de Chocolate Meio Amargo")
           .produto
)
print(f"Bolo Personalizado: {bolo_personalizado}")


# 2. Usando o Diretor (Confeiteiro) para receitas prontas
print("\n--- Usando o Confeiteiro para receitas prontas ---")
confeiteiro = Confeiteiro(builder)

# Pedindo um bolo Floresta Negra
confeiteiro.fazer_bolo_floresta_negra()
bolo_floresta_negra = builder.produto  # O builder agora contém o bolo pronto
print(f"Receita do Confeiteiro: {bolo_floresta_negra}")

# Pedindo um bolo de Festa
confeiteiro.fazer_bolo_de_festa()
bolo_festa = builder.produto
print(f"Receita do Confeiteiro: {bolo_festa}")
