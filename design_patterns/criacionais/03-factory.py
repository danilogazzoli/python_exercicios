from __future__ import annotations
from abc import ABC, abstractmethod

# O padrão Factory Method define uma interface para criar um objeto,
# mas deixa as subclasses decidirem qual classe instanciar.
# Ele permite que uma classe adie a instanciação para as subclasses.

# --- 1. Product Interface ---
# A interface para os objetos que o método de fábrica irá criar.
class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass

# --- 2. Concrete Products ---
# Implementações concretas da interface do produto.
class Circulo(Forma):
    def desenhar(self):
        return "Desenhando um círculo"

class Quadrado(Forma):
    def desenhar(self):
        return "Desenhando um quadrado"

# --- 3. Creator (Abstract Factory) ---
# Declara o "método de fábrica" que retorna um objeto do tipo Produto.
# Pode também definir uma implementação padrão.
class FabricaDeFormas(ABC):
    @abstractmethod
    def criar_forma(self) -> Forma:
        """Este é o Factory Method."""
        pass

    def alguma_operacao(self) -> str:
        """
        O código principal do Creator não depende do produto concreto,
        pois ele usa o método de fábrica para obter o objeto.
        """
        produto = self.criar_forma()
        resultado = f"Fábrica: A operação funcionou com {produto.desenhar()}"
        return resultado

# --- 4. Concrete Creators ---
# Sobrescrevem o método de fábrica para retornar uma instância de um Produto concreto.
class FabricaDeCirculos(FabricaDeFormas):
    def criar_forma(self) -> Forma:
        return Circulo()

class FabricaDeQuadrados(FabricaDeFormas):
    def criar_forma(self) -> Forma:
        return Quadrado()

# --- 5. Client Code ---
# O código cliente trabalha com uma instância de um Creator concreto,
# embora através de sua interface abstrata.
def codigo_cliente(fabrica: FabricaDeFormas):
    """
    O cliente não sabe qual fábrica está recebendo, apenas que pode
    chamar seus métodos.
    """
    print(f"Cliente: Não conheço a classe da fábrica, mas ela funciona.\n"
          f"{fabrica.alguma_operacao()}", end="\n\n")

print("App: Lançado com a Fábrica de Círculos.")
codigo_cliente(FabricaDeCirculos())

print("App: Lançado com a Fábrica de Quadrados.")
codigo_cliente(FabricaDeQuadrados())


#Extensibilidade (Princípio Aberto/Fechado): Para adicionar uma nova forma, como Triangulo, você só precisa criar a classe Triangulo e uma FabricaDeTriangulos. Você não precisa tocar no código existente das outras fábricas ou do código cliente.

#Desacoplamento: O código cliente (codigo_cliente) depende apenas das interfaces abstratas (Forma e FabricaDeFormas), não das implementações concretas. Isso torna o sistema mais flexível e fácil de manter.

#Responsabilidade Única: Cada classe de fábrica concreta tem uma única e clara responsabilidade: criar um tipo específico de objeto.

'''
Diferença entre factory e abstract factory:

Factory Method (03-factory.py) é sobre criar um objeto, mas deixar que as subclasses decidam qual tipo específico de objeto criar. É um método que é sobrescrito.

* Baseado em herança. As subclasses (FabricaDeCirculos, FabricaDeQuadrados) sobrescrevem um único "método de fábrica" da classe pai.
* Focado na criação de um único produto.
* Retorna uma instância de um único produto.

Abstract Factory (01-abstract_factory.py) é sobre criar famílias de objetos relacionados, garantindo que os objetos criados juntos sejam compatíveis. É um objeto que tem vários métodos de fábrica.

* Baseado em composição. O Abstract Factory (como FabricaDeFormas) pode ter vários métodos de fábrica (criar_forma, criar_outro_produto).
* Focado na criação de famílias de produtos.
* Retorna instâncias de produtos relacionados.

'''