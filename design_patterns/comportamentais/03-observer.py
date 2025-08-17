from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# O padrão Observer define uma dependência um-para-muitos entre objetos,
# de modo que, quando um objeto (o sujeito) muda de estado, todos os seus
# dependentes (observadores) são notificados e atualizados automaticamente.

# --- 1. A Interface do Sujeito (Subject) ---
# Define métodos para adicionar, remover e notificar observadores.
class ISujeito(ABC):
    @abstractmethod
    def adicionar_observador(self, observador: IObservador) -> None:
        pass

    @abstractmethod
    def remover_observador(self, observador: IObservador) -> None:
        pass

    @abstractmethod
    def notificar_observadores(self) -> None:
        pass

# --- 2. A Interface do Observador (Observer) ---
# Define o método de atualização que os sujeitos usarão para notificar.
class IObservador(ABC):
    @abstractmethod
    def atualizar(self, sujeito: ISujeito) -> None:
        pass

# --- 3. O Sujeito Concreto (Concrete Subject) ---
# Mantém o estado e notifica os observadores quando o estado muda.
class Termometro(ISujeito):
    _temperatura: float = 0.0

    def __init__(self):
        self._observadores: List[IObservador] = []

    def adicionar_observador(self, observador: IObservador) -> None:
        print("Termômetro: Adicionando um observador.")
        self._observadores.append(observador)

    def remover_observador(self, observador: IObservador) -> None:
        print("Termômetro: Removendo um observador.")
        self._observadores.remove(observador)

    def notificar_observadores(self) -> None:
        print("Termômetro: Notificando observadores...")
        for observador in self._observadores:
            observador.atualizar(self)

    def set_temperatura(self, temperatura: float) -> None:
        print(f"\nTermômetro: A temperatura mudou para {temperatura}°C.")
        self._temperatura = temperatura
        self.notificar_observadores()

    @property
    def temperatura(self) -> float:
        return self._temperatura

# --- 4. Observadores Concretos (Concrete Observers) ---
# Reagem às atualizações do sujeito ao qual estão inscritos.
class Display(IObservador):
    def atualizar(self, sujeito: Termometro) -> None:
        # O observador puxa o estado que precisa do sujeito.
        print(f"Display: Temperatura atualizada para {sujeito.temperatura}°C")

class Alarme(IObservador):
    _limite_temperatura = 30.0

    def atualizar(self, sujeito: Termometro) -> None:
        if sujeito.temperatura > self._limite_temperatura:
            print(f"Alarme: ALERTA! Temperatura ({sujeito.temperatura}°C) acima do limite de {self._limite_temperatura}°C!")

# --- Código Cliente ---
termometro = Termometro()
display = Display()
alarme = Alarme()
termometro.adicionar_observador(display)
termometro.adicionar_observador(alarme)

termometro.set_temperatura(25)
termometro.set_temperatura(32)

termometro.remover_observador(alarme)

termometro.set_temperatura(35) # O alarme não será mais notificado
