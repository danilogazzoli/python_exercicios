from abc import ABC, abstractmethod

# --- Abstract Products ---
# Define the interface for a family of objects.

class Botao:
    @abstractmethod
    def renderizar(self):
        pass

class Checkbox:
    @abstractmethod
    def renderizar(self):
        pass

# --- Concrete Products ---
# Implementations for the "Desktop" family.

class BotaoDesktop(Botao):
    def renderizar(self):
        return "Botão de Desktop"

class CheckboxDesktop(Checkbox):
    def renderizar(self):
        return "Checkbox de Desktop"

# Implementations for the "Web" family.

class BotaoWeb(Botao):
    def renderizar(self):
        return "Botão de Web"

class CheckboxWeb(Checkbox):
    def renderizar(self):
        return "Checkbox de Web"

# --- Abstract Factory ---
# Declares an interface for operations that create abstract product objects.
# It declares a set of methods for creating abstract products (e.g., criar_botao, criar_checkbox). It doesn't know how they are made, just that they can be made.

class FabricaUI(ABC):
    @abstractmethod
    def criar_botao(self):
        pass

    @abstractmethod
    def criar_checkbox(self):
        pass

# --- Concrete Factories ---
# Each concrete factory creates a specific family of products.
# FabricaDesktop knows how to create a BotaoDesktop and a CheckboxDesktop.
# FabricaWeb knows how to create a BotaoWeb and a CheckboxWeb. It guarantees that all products from a single factory are from the same family (all Desktop or all Web), ensuring they look and work correctly together.

class FabricaDesktop(FabricaUI):
    def criar_botao(self):
        return BotaoDesktop()

    def criar_checkbox(self):
        return CheckboxDesktop()

class FabricaWeb(FabricaUI):
    def criar_botao(self):
        return BotaoWeb()

    def criar_checkbox(self):
        return CheckboxWeb()

# --- Client Code ---
# The client works with factories and products only through abstract interfaces.

def montar_interface(fabrica: FabricaUI):
    print(f"Montando interface com a fábrica: {fabrica.__class__.__name__}")
    botao = fabrica.criar_botao()
    checkbox = fabrica.criar_checkbox()

    print(f" - {botao.renderizar()}")
    print(f" - {checkbox.renderizar()}")
    print("-" * 20)

print("Executando cliente com a fábrica de Desktop:")
montar_interface(FabricaDesktop())

print("Executando cliente com a fábrica da Web:")
montar_interface(FabricaWeb())

# Com o Abstract Factory, o código cliente não depende das classes concretas dos produtos.
# Ele trabalha com famílias de objetos (Desktop, Web) através de uma interface abstrata.
# Trocar a família de produtos é tão simples quanto instanciar uma fábrica diferente.

#problem: You want your main application code (the "client") to be able to say "give me a button" and "give me a checkbox" without needing to know if it's for Desktop or Web. The client shouldn't have if/else statements all over the place to decide which kind of button to create.

# Key Benefits Summarized
# Isolation: You isolate the concrete classes from the client. The client code has no idea which specific button class it's using.
# Easy Exchangeability: You can switch the entire family of products at once by simply changing the factory instance.
# Guaranteed Consistency: When you use a factory, you are guaranteed that the created objects belong to the same family and are compatible with each other. You'll never get a BotaoWeb mixed with a CheckboxDesktop.