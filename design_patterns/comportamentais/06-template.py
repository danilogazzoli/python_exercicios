from abc import ABC, abstractmethod

# O padrão Template Method define o esqueleto de um algoritmo em uma operação,
# adiando alguns passos para as subclasses. Ele permite que as subclasses
# redefinam certos passos de um algoritmo sem alterar a estrutura do algoritmo.

# --- 1. A Classe Abstrata (Abstract Class) ---
# Contém o "método modelo" (template method) e as operações primitivas abstratas.
class ValidadorDocumento(ABC):
    """
    Define o esqueleto do algoritmo de validação.
    """
    def validar(self, documento: str) -> bool:
        """
        Este é o Template Method. Ele define a sequência de passos do algoritmo.
        """
        print(f"\n--- Validando '{documento}' com {self.__class__.__name__} ---")
        documento_limpo = self.limpar_documento(documento) # Chamada do Hook
        
        if not self.verificar_formato(documento_limpo):
            print(">>> Documento inválido: formato incorreto.")
            return False
        
        if not self.validar_digitos(documento_limpo):
            print(">>> Documento inválido: dígitos verificadores não batem.")
            return False
        
        print(">>> Documento válido!")
        return True

    # --- Passos Abstratos (Obrigatórios) ---
    @abstractmethod
    def verificar_formato(self, documento: str) -> bool:
        """Operação primitiva: deve ser implementada pelas subclasses."""
        pass

    @abstractmethod
    def validar_digitos(self, documento: str) -> bool:
        """Operação primitiva: deve ser implementada pelas subclasses."""
        pass

    # --- Hook (Gancho) ---
    def limpar_documento(self, documento: str) -> str:
        """
        Um "hook" é um passo opcional com uma implementação padrão.
        Subclasses podem (mas não precisam) sobrescrevê-lo.
        """
        print("Hook: Removendo pontuação padrão ('.', '-', '/')...")
        return documento.replace(".", "").replace("-", "").replace("/", "")

# --- 2. Classes Concretas (Concrete Classes) ---
# Implementam os passos variáveis do algoritmo.
class ValidarCPF(ValidadorDocumento):
    def verificar_formato(self, documento: str) -> bool:
        print(f"Passo 1 (CPF): Verificando se '{documento}' tem 11 dígitos.")
        return len(documento) == 11 and documento.isdigit()

    def validar_digitos(self, documento: str) -> bool:
        print("Passo 2 (CPF): Validando dígitos verificadores (lógica simulada).")
        return True # Lógica de validação real seria implementada aqui

# --- Código Cliente ---
validador_cpf = ValidarCPF()
validador_cpf.validar("123.456.789-00")

validador_cpf.validar("1234567890") # Formato inválido