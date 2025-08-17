import threading

# O padrão Singleton garante que uma classe tenha apenas uma instância e fornece
# um ponto de acesso global a essa instância.

# --- A Metaclass-based Singleton Implementation ---
# Esta é uma forma mais robusta e thread-safe de implementar o padrão.

class SingletonMeta(type):
    """
    Esta é uma metaclasse para o Singleton. Ela armazena uma instância de cada classe
    que a utiliza e garante que apenas uma instância seja criada.
    A lógica de bloqueio (threading.Lock) a torna segura para uso em ambientes com múltiplas threads.
    """
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Este método é chamado quando você faz `NomeDaClasse()`.
        Ele intercepta a chamada de criação da instância.
        """
        # O bloqueio garante que duas threads não possam criar a instância simultaneamente.
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

# --- O Singleton Concreto ---
# A classe agora usa a metaclasse para controlar sua instanciação.
# O método __init__ só será chamado na primeira vez que a instância for criada.

class ConexaoBanco(metaclass=SingletonMeta):
    def __init__(self):
        """
        O inicializador. Graças à metaclasse, este código
        só será executado uma vez.
        """
        # Simula uma configuração inicial custosa
        print("Configurando e estabelecendo a conexão com o banco de dados...")
        self.host = "localhost"
        self.user = "admin"
        self.status = "Conectado"

    def __str__(self):
        return f"Conexão com {self.host} como {self.user}. Status: {self.status}"

# --- Código Cliente ---
print("Tentando criar a primeira conexão...")
conexao1 = ConexaoBanco()
print(f"Conexão 1: {conexao1}")

print("\nTentando criar a segunda conexão...")
conexao2 = ConexaoBanco()
print(f"Conexão 2: {conexao2}")

# Verificando se as instâncias são as mesmas e compartilham o mesmo estado
print(f"\nconexao1 is conexao2? {conexao1 is conexao2}")

conexao2.status = "Desconectado"
print(f"\nEstado alterado em conexao2. Verificando conexao1: {conexao1}")