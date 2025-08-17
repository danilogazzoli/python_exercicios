from __future__ import annotations
from abc import ABC, abstractmethod

# O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda.
# O objeto parece mudar de classe. A lógica de estado é encapsulada em classes separadas.

# --- 1. A Interface do Estado (State) ---
# Declara métodos que todos os estados concretos devem implementar e fornece uma
# referência de volta para o objeto de contexto.
class Estado(ABC):
    _contexto: Reprodutor

    @property
    def contexto(self) -> Reprodutor:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Reprodutor) -> None:
        self._contexto = contexto

    @abstractmethod
    def pressionar_play(self) -> None:
        pass

    @abstractmethod
    def pressionar_pause(self) -> None:
        pass

# --- 2. O Contexto (Context) ---
# Define a interface de interesse para os clientes e mantém uma instância de um
# estado concreto que define o estado atual.
class Reprodutor:
    _estado: Estado = None

    def __init__(self):
        # O reprodutor começa no estado 'Parado'
        self.transicionar_para(EstadoParado())

    def transicionar_para(self, estado: Estado) -> None:
        """O Contexto permite alterar o objeto Estado em tempo de execução."""
        print(f"Reprodutor: Transicionando para o estado '{type(estado).__name__}'")
        self._estado = estado
        self._estado.contexto = self

    def pressionar_play(self):
        """O Contexto delega o comportamento para o objeto de estado atual."""
        self._estado.pressionar_play()

    def pressionar_pause(self):
        self._estado.pressionar_pause()

# --- 3. Estados Concretos (Concrete States) ---
# Implementam os comportamentos associados a um estado do Contexto.

class EstadoParado(Estado):
    def pressionar_play(self) -> None:
        print("Iniciando a reprodução...")
        self.contexto.transicionar_para(EstadoReproduzindo())

    def pressionar_pause(self) -> None:
        print("Ação inválida: O reprodutor já está parado.")

class EstadoReproduzindo(Estado):
    def pressionar_play(self) -> None:
        print("Ação inválida: O reprodutor já está tocando.")

    def pressionar_pause(self) -> None:
        print("Pausando a reprodução...")
        self.contexto.transicionar_para(EstadoPausado())

class EstadoPausado(Estado):
    def pressionar_play(self) -> None:
        print("Retomando a reprodução...")
        self.contexto.transicionar_para(EstadoReproduzindo())

    def pressionar_pause(self) -> None:
        print("Ação inválida: O reprodutor já está pausado.")

# --- Código Cliente ---
reprodutor = Reprodutor() # Começa no estado Parado

print("\n--- Testando a máquina de estados ---")
reprodutor.pressionar_play()   # Parado -> Reproduzindo
reprodutor.pressionar_pause()  # Reproduzindo -> Pausado
reprodutor.pressionar_pause()  # Pausado -> Ação inválida
reprodutor.pressionar_play()   # Pausado -> Reproduzindo
reprodutor.pressionar_play()   # Reproduzindo -> Ação inválida


#A classe Reprodutor mantém um estado atual e delega a lógica de mudança para a classe correspondente. 
# Cada estado sabe para qual outro deve transicionar ao pressionar o botão, evitando condicionais dentro do reprodutor.