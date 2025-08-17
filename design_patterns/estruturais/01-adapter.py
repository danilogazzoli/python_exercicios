from abc import ABC, abstractmethod

# O padrão Adapter permite que objetos com interfaces incompatíveis colaborem.
# Ele atua como um tradutor entre duas interfaces diferentes.

# --- 1. A Interface Alvo (Target) ---
# Esta é a interface que o código cliente espera usar.
class IPagamentoGateway(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor: float) -> str:
        pass

# --- 2. As Classes Incompatíveis (Adaptees) ---
# Estas são as classes existentes que queremos integrar, mas que possuem interfaces diferentes.
class PayPal:
    def pagar(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com PayPal"

class Stripe:
    def processar_pagamento(self, quantia: float) -> str:
        return f"Pagamento de R${quantia:.2f} processado com Stripe"

# --- 3. Os Adapters Concretos ---
# Cada adapter implementa a interface alvo e envolve (wraps) um objeto incompatível.
# O PagamentoAdapter atua como um intermediário, aceitando qualquer um desses métodos e oferecendo uma interface comum através do método realizar_pagamento.
#Ao criar instâncias do PagamentoAdapter com PayPal ou Stripe, é possível chamar o método realizar_pagamento consistentemente, sem se preocupar com as diferenças nas implementações de cada classe, garantindo flexibilidade e extensibilidade no código.
#Dessa maneira, as diferenças entre as interfaces são abstraídas em uma única classe. Isso permite integrar facilmente novos métodos de pagamento sem alterar o restante do sistema, promovendo um design mais limpo, flexível e preparado para mudanças.

class PayPalAdapter(IPagamentoGateway):
    def __init__(self, paypal: PayPal):
        self._paypal = paypal

    def realizar_pagamento(self, valor: float) -> str:
        # O adapter traduz a chamada do método da interface alvo
        # para o método específico da classe adaptada.
        return self._paypal.pagar(valor)

class StripeAdapter(IPagamentoGateway):
    def __init__(self, stripe: Stripe):
        self._stripe = stripe

    def realizar_pagamento(self, valor: float) -> str:
        # A tradução aqui é de 'valor' para 'quantia'.
        return self._stripe.processar_pagamento(quantia=valor)

# --- 4. O Código Cliente ---
# O cliente interage apenas com a interface alvo, sem conhecer os detalhes
# das classes de pagamento subjacentes.
def processar_compra(gateway: IPagamentoGateway, total: float):
    print("Iniciando processo de pagamento...")
    resultado = gateway.realizar_pagamento(total)
    print(resultado)
    print("Processo de pagamento finalizado.\n")

# --- Uso ---
print("--- Usando o sistema de pagamento com Adapters ---")

# 1. Criamos as instâncias dos sistemas de pagamento originais
paypal_gateway = PayPal()
stripe_gateway = Stripe()

# 2. Envolvemos as instâncias em seus respectivos adapters
adaptador_paypal = PayPalAdapter(paypal_gateway)
adaptador_stripe = StripeAdapter(stripe_gateway)

# 3. O cliente usa os adapters através da interface comum, sem se preocupar com a implementação
processar_compra(adaptador_paypal, 150.75)
processar_compra(adaptador_stripe, 300.50)