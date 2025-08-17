from __future__ import annotations
from abc import ABC, abstractmethod

# O padrão Strategy define uma família de algoritmos, encapsula cada um deles
# e os torna intercambiáveis. Ele permite que o algoritmo varie independentemente
# dos clientes que o utilizam.


#Definir um Contrato Formal: Usar uma classe base abstrata (ABC) para a interface da estratégia, garantindo que todos os algoritmos tenham a mesma assinatura.
#Permitir a Troca em Tempo de Execução: Uma das maiores vantagens do padrão Strategy é a capacidade de alterar o algoritmo dinamicamente. 
# O contexto deve ter um método para trocar a estratégia atual.
#Melhorar a Clareza: Usar type hints e nomes que seguem a terminologia do padrão (IEstrategia, Contexto) torna o código mais legível e seguro.

# --- 1. A Interface da Estratégia (Strategy) ---
# Declara uma operação comum a todos os algoritmos suportados.
class IEstrategiaRecomendacao(ABC):
    @abstractmethod
    def recomendar(self, usuario_id: str) -> list[str]:
        """
        Executa o algoritmo de recomendação e retorna uma lista de itens.
        """
        pass

# --- 2. Estratégias Concretas (Concrete Strategies) ---
# Implementam o algoritmo seguindo a interface da Estratégia.

class RecomendacaoColaborativa(IEstrategiaRecomendacao):
    def recomendar(self, usuario_id: str) -> list[str]:
        print(f"Estratégia: Usando filtragem colaborativa para o usuário '{usuario_id}'.")
        # Lógica real: buscar usuários similares e recomendar seus itens.
        return ["Filme A", "Livro B", "Música C"]

class RecomendacaoConteudo(IEstrategiaRecomendacao):
    def recomendar(self, usuario_id: str) -> list[str]:
        print(f"Estratégia: Usando filtragem baseada em conteúdo para o usuário '{usuario_id}'.")
        # Lógica real: buscar itens com atributos similares aos que o usuário gostou.
        return ["Filme D", "Livro E", "Música F"]

class RecomendacaoHibrida(IEstrategiaRecomendacao):
    def recomendar(self, usuario_id: str) -> list[str]:
        print(f"Estratégia: Usando algoritmo híbrido para o usuário '{usuario_id}'.")
        # Lógica real: combinar as duas abordagens.
        return ["Filme A", "Livro E", "Música G"]

# --- 3. O Contexto (Context) ---
# Mantém uma referência a um objeto Estratégia e o utiliza para executar o algoritmo.
# Permite que a estratégia seja trocada em tempo de execução.
class SistemaRecomendacao:
    _estrategia: IEstrategiaRecomendacao

    def __init__(self, estrategia: IEstrategiaRecomendacao):
        """
        O Contexto aceita uma estratégia através do construtor e também
        fornece um setter para alterá-la em tempo de execução.
        """
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: IEstrategiaRecomendacao):
        """Permite a troca da estratégia em tempo de execução."""
        print("\nContexto: Trocando de estratégia...")
        self._estrategia = estrategia

    def obter_recomendacoes(self, usuario_id: str):
        """
        O Contexto delega o trabalho para o objeto Estratégia em vez de
        implementar múltiplas versões do algoritmo por conta própria.
        """
        print("Contexto: Solicitando recomendações...")
        recomendacoes = self._estrategia.recomendar(usuario_id)
        print(f"Contexto: Recomendações para '{usuario_id}': {', '.join(recomendacoes)}")

# --- 4. Código Cliente ---
# O cliente escolhe uma estratégia concreta e a passa para o contexto.

# Começa com a estratégia colaborativa
contexto = SistemaRecomendacao(RecomendacaoColaborativa())
contexto.obter_recomendacoes("usuario-123")

# Troca para a estratégia baseada em conteúdo em tempo de execução
contexto.set_estrategia(RecomendacaoConteudo())
contexto.obter_recomendacoes("usuario-123")

# Troca para a estratégia híbrida
contexto.set_estrategia(RecomendacaoHibrida())
contexto.obter_recomendacoes("usuario-456")


#A classe SistemaRecomendacao permite alterar a estratégia de recomendação em tempo de execução, sem precisar modificar a lógica interna da classe principal.

#Esse padrão promove um design mais limpo, flexível e escalável, permitindo que você altere facilmente o comportamento do sistema sem a necessidade de modificar o código que utiliza essas estratégias.