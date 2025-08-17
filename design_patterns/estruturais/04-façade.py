# O padrão Facade (Fachada) fornece uma interface simplificada para uma biblioteca,
# um framework ou qualquer outro conjunto complexo de classes.

# --- 1. Os Subsistemas Complexos ---
# Estas são as classes que fazem o trabalho pesado. O cliente não quer
# (ou não precisa) interagir com elas diretamente.

class Estoque:
    """Gerencia a disponibilidade de produtos."""
    def tem_no_estoque(self, produto: str) -> bool:
        print(f"Verificando estoque para o produto '{produto}'...")
        # Lógica complexa de verificação de estoque aqui
        if produto == "Notebook":
            print("-> Produto disponível.")
            return True
        print("-> Produto indisponível.")
        return False

class Pagamento:
    """Processa transações financeiras."""
    def processar_pagamento(self, cliente_id: str, valor: float) -> bool:
        print(f"Processando pagamento de R${valor:.2f} para o cliente '{cliente_id}'...")
        # Lógica de comunicação com gateway de pagamento
        print("-> Pagamento aprovado.")
        return True

class Notificacao:
    """Envia notificações para o cliente."""
    def enviar_email_confirmacao(self, cliente_id: str, produto: str) -> None:
        print(f"Enviando e-mail de confirmação para '{cliente_id}' sobre o produto '{produto}'.")
        print("-> E-mail enviado.")

# --- 2. A Fachada (Facade) ---
# Fornece uma interface simples e unificada para o conjunto de subsistemas.

class GerenciadorDePedidosFacade:
    """
    Fornece uma interface simplificada para realizar um pedido,
    orquestrando os subsistemas de Estoque, Pagamento e Notificação.
    """
    def __init__(self, estoque: Estoque, pagamento: Pagamento, notificacao: Notificacao):
        """
        A fachada não cria os subsistemas, mas os recebe via injeção de dependência.
        Isso desacopla a fachada das implementações concretas dos subsistemas.
        """
        self._estoque = estoque
        self._pagamento = pagamento
        self._notificacao = notificacao

    def realizar_pedido(self, produto: str, cliente_id: str, valor: float) -> str:
        """
        Este método é um exemplo de como a fachada simplifica um processo complexo.
        O cliente só precisa chamar este método, em vez de chamar vários métodos
        dos subsistemas na ordem correta.
        """
        print("\n--- Iniciando processo de pedido via Fachada ---")
        
        if not self._estoque.tem_no_estoque(produto):
            return "Pedido falhou: Produto fora de estoque."

        if not self._pagamento.processar_pagamento(cliente_id, valor):
            return "Pedido falhou: Pagamento recusado."

        self._notificacao.enviar_email_confirmacao(cliente_id, produto)

        print("--- Processo de pedido finalizado com sucesso! ---")
        return f"Pedido para '{produto}' realizado com sucesso."

# --- 3. O Código Cliente ---
# O cliente interage com o sistema através da fachada.

# Em uma aplicação real, estas instâncias poderiam vir de um container de Injeção de Dependência.
estoque_subsystem = Estoque()
pagamento_subsystem = Pagamento()
notificacao_subsystem = Notificacao()

# O cliente cria a fachada, injetando as dependências.
gerenciador = GerenciadorDePedidosFacade(
    estoque=estoque_subsystem,
    pagamento=pagamento_subsystem,
    notificacao=notificacao_subsystem
)

# O cliente realiza a operação complexa com uma única chamada de método.
resultado_sucesso = gerenciador.realizar_pedido(
    produto="Notebook",
    cliente_id="cliente-123",
    valor=3000.00
)
print(f"\nResultado final para o cliente: {resultado_sucesso}")

# Tentativa com produto fora de estoque
resultado_falha = gerenciador.realizar_pedido(
    produto="Smartphone",
    cliente_id="cliente-456",
    valor=1500.00
)
print(f"\nResultado final para o cliente: {resultado_falha}")