
from __future__ import annotations
from abc import ABC, abstractmethod

# Os padrões comportamentais focam em como os objetos interagem e distribuem responsabilidades.
# Eles são projetados para gerenciar algoritmos, relacionamentos e a comunicação entre objetos,
# resultando em sistemas mais flexíveis, coesos e de fácil manutenção.
#
# Ao contrário dos padrões criacionais (criação) e estruturais (composição), os comportamentais
# se concentram nos padrões de comunicação, tornando as interações mais claras e o
# acoplamento entre os componentes mais baixo.

# O padrão Command transforma uma solicitação em um objeto autônomo que contém
# todas as informações sobre a solicitação. Isso permite parametrizar métodos com
# diferentes solicitações, enfileirar ou registrar solicitações e suportar
# operações que podem ser desfeitas.

# --- 1. A Interface do Comando (Command) ---
# Declara um método para executar a ação e, crucialmente, um para desfazê-la.
class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

# --- 2. O Receptor (Receiver) ---
# Contém a lógica de negócio real. Sabe como realizar as operações.
class EditorDeTexto:
    def __init__(self):
        self.conteudo = ""

    def adicionar_texto(self, texto: str):
        self.conteudo += texto

    def apagar_texto(self, tamanho: int):
        self.conteudo = self.conteudo[:-tamanho]

# --- 3. Comandos Concretos (Concrete Commands) ---
# Implementam a interface e encapsulam a lógica para chamar o Receiver.
class ComandoColar(ICommand):
    def __init__(self, editor: EditorDeTexto, texto: str):
        self._editor = editor
        self._texto = texto

    def execute(self) -> None:
        print(f"Comando: Colando '{self._texto}'")
        self._editor.adicionar_texto(self._texto)

    def undo(self) -> None:
        print(f"Desfazendo: Removendo '{self._texto}'")
        self._editor.apagar_texto(len(self._texto))

# --- 4. O Invocador (Invoker) ---
# Pede ao comando para executar a solicitação. Mantém o histórico de comandos.
class GerenciadorDeComandos:
    def __init__(self):
        self._historico: list[ICommand] = []

    def executar_comando(self, comando: ICommand) -> None:
        comando.execute()
        self._historico.append(comando)

    def desfazer_ultimo_comando(self) -> None:
        if not self._historico:
            print("Nada para desfazer.")
            return
        
        ultimo_comando = self._historico.pop()
        ultimo_comando.undo()

# --- 5. O Código Cliente ---
editor = EditorDeTexto()
invocador = GerenciadorDeComandos()

print(f"Estado inicial: '{editor.conteudo}'")
print("-" * 20)

# Executando comandos
comando1 = ComandoColar(editor, "Olá, ")
invocador.executar_comando(comando1)
print(f"Estado atual: '{editor.conteudo}'")
print("-" * 20)

comando2 = ComandoColar(editor, "mundo!")
invocador.executar_comando(comando2)
print(f"Estado atual: '{editor.conteudo}'")
print("-" * 20)

# Desfazendo comandos
invocador.desfazer_ultimo_comando()
print(f"Estado após undo: '{editor.conteudo}'")
print("-" * 20)

invocador.desfazer_ultimo_comando()
print(f"Estado após undo: '{editor.conteudo}'")
print("-" * 20)

invocador.desfazer_ultimo_comando() # Tentando desfazer com histórico vazio


# O código desacopla a lógica das ações do editor de texto, tornando os comandos reutilizáveis e flexíveis.
# A classe abstrata Comando define a estrutura básica para qualquer comando. ComandoColar recebe uma referência ao editor e adiciona um texto ao conteúdo, enquanto ComandoCopiar retorna o conteúdo atual.
# A classe EditorDeTexto mantém um histórico de comandos e executa cada um por meio do método executar_comando().
# No uso, um comando de colar adiciona o texto ao editor, e um comando de copiar retorna esse conteúdo.
# Assim, você pode adicionar novos comandos sem alterar o código existente, implementar facilmente funcionalidades como desfazer e refazer e gerenciar o histórico de ações. Esse padrão promove um design modular, limpo e preparado para evolução.
