from __future__ import annotations
from abc import ABC, abstractmethod

# O padrão Decorator anexa novas responsabilidades a um objeto dinamicamente.
# Decorators fornecem uma alternativa flexível à herança para estender a funcionalidade.

# --- 1. A Interface do Componente (Component) ---
# Define a interface para os objetos que podem ter responsabilidades adicionadas.
class INotificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> str:
        pass

# --- 2. O Componente Concreto (Concrete Component) ---
# Um objeto ao qual funcionalidades extras podem ser anexadas.
class NotificadorEmail(INotificador):
    def enviar(self, mensagem: str) -> str:
        return f"Enviando e-mail: {mensagem}"

class NotificadorSMS(INotificador):
    def enviar(self, mensagem: str) -> str:
        return f"Enviando SMS: {mensagem}"

# --- 3. O Decorator Base (Base Decorator) ---
# Mantém uma referência a um objeto Componente e define uma interface
# que está em conformidade com a interface do Componente.
class BaseNotificadorDecorator(INotificador):
    _notificador: INotificador = None

    def __init__(self, notificador: INotificador):
        self._notificador = notificador

    def enviar(self, mensagem: str) -> str:
        """O Decorator base simplesmente delega o trabalho para o componente envolvido."""
        return self._notificador.enviar(mensagem)

# --- 4. Decorators Concretos (Concrete Decorators) ---
# Adicionam responsabilidades ao componente.

class LogDecorator(BaseNotificadorDecorator):
    """Adiciona um log antes de enviar a notificação."""
    def enviar(self, mensagem: str) -> str:
        log = "Registrando log da mensagem..."
        resultado_original = self._notificador.enviar(mensagem)
        return f"{log}\n{resultado_original}"

class PrioridadeDecorator(BaseNotificadorDecorator):
    """Adiciona uma marca de prioridade à mensagem."""
    def enviar(self, mensagem: str) -> str:
        mensagem_prioritaria = f"[PRIORITÁRIO] {mensagem}"
        return self._notificador.enviar(mensagem_prioritaria)

class CriptografiaDecorator(BaseNotificadorDecorator):
    """Simula a criptografia da mensagem."""
    def enviar(self, mensagem: str) -> str:
        # Em um caso real, aqui haveria uma lógica de criptografia.
        mensagem_criptografada = f"<{mensagem[::-1]}>" # Simples inversão como exemplo
        print(f"Criptografando mensagem: '{mensagem}' -> '{mensagem_criptografada}'")
        return self._notificador.enviar(mensagem_criptografada)

# --- Código Cliente ---
# O cliente pode compor os decorators de forma flexível.

mensagem = "Sistema fora do ar!"

print("--- Cenário 1: E-mail com log e prioridade ---")
notificador_base = NotificadorEmail()
notificador_com_log = LogDecorator(notificador_base)
notificador_final = PrioridadeDecorator(notificador_com_log)
print("Resultado:\n" + notificador_final.enviar(mensagem))

print("\n" + "="*40 + "\n")

print("--- Cenário 2: SMS com criptografia e log ---")
# A ordem dos decorators importa!
notificador_sms = NotificadorSMS()
notificador_criptografado = CriptografiaDecorator(notificador_sms)
notificador_final_sms = LogDecorator(notificador_criptografado)
print("Resultado:\n" + notificador_final_sms.enviar(mensagem))