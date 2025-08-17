"""
Exemplos de Clean Code em Python

Este arquivo demonstra várias práticas de codificação, comparando
abordagens "ruins" (Bad Practice) com abordagens "boas" (Good Practice)
para ilustrar os princípios do Clean Code.
"""
import os

# --- Exemplo 1: Nomes de Variáveis e Funções ---
print("--- Exemplo 1: Nomes Descritivos ---")

# Bad Practice: Nomes curtos e não descritivos
def calc(a, b, c):
    return a + b - c

# Good Practice: Nomes claros que revelam a intenção
def calcular_preco_final(preco_item, imposto, desconto):
    """Calcula o preço final de um item aplicando imposto e desconto."""
    return preco_item + (preco_item * imposto) - desconto

print(f"Bom: {calcular_preco_final(100, 0.07, 10):.2f}")


# --- Exemplo 2: Funções com Responsabilidade Única (Single Responsibility) ---
print("\n--- Exemplo 2: Responsabilidade Única ---")

# Bad Practice: Uma função que faz tudo (filtra, calcula, imprime)
def processar_dados_ruim(dados_brutos):
    # 1. Filtra dados
    dados_filtrados = [x for x in dados_brutos if x > 0]
    if not dados_filtrados:
        return None
    # 2. Calcula a média
    media = sum(dados_filtrados) / len(dados_filtrados)
    # 3. Imprime o resultado
    print(f"Média (ruim): {media}")
    return dados_filtrados

# Good Practice: Funções separadas para cada tarefa
def filtrar_dados_positivos(dados):
    """Retorna apenas os números positivos de uma lista."""
    return [x for x in dados if x > 0]

def calcular_media(dados):
    """Calcula a média de uma lista de números."""
    if not dados:
        return 0
    return sum(dados) / len(dados)

def exibir_resultado(descricao, valor):
    """Exibe um resultado formatado."""
    print(f"{descricao}: {valor:.2f}")

# Uso da boa prática:
dados_brutos = [10, -5, 20, 0, 15]
dados_filtrados = filtrar_dados_positivos(dados_brutos)
media = calcular_media(dados_filtrados)
exibir_resultado("Média (bom)", media)


# --- Exemplo 3: Tratamento de Erros ---
print("\n--- Exemplo 3: Tratamento de Erros ---")

# Bad Practice: Retornar tipos mistos (número ou string/None) ou nao tratar o código
def dividir_ruim(x, y):
    return x / y

def dividir_ruim2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # Misturar tipos de retorno torna o código cliente frágil
        return "Erro: Divisão por zero"

# Good Practice: Levantar exceções para falhas
def dividir_bom(x, y):
    """Divide x por y, levantando uma exceção clara em caso de erro."""
    try:
        return x / y
    except ZeroDivisionError as e:
        # Levanta uma exceção semântica para um erro de valor.
        raise ValueError("O denominador não pode ser zero.") from e
    except TypeError:
        # Levanta uma exceção semântica para um erro de tipo.
        raise TypeError("Ambos os operandos devem ser números.")

# Uso da boa prática:
print("Testando divisão por zero:")
try:
    dividir_bom(10, 0)
except ValueError as e:
    print(f"-> Erro capturado (bom): {e}")

print("\nTestando divisão com tipo inválido:")
try:
    dividir_bom(10, "a")
except TypeError as e:
    print(f"-> Erro capturado (bom): {e}")


# --- Exemplo 4: Evitar Duplicação de Código (DRY - Don't Repeat Yourself) ---
print("\n--- Exemplo 4: Não se Repita (DRY) ---")
produto_exemplo = {'name': 'Notebook', 'price': 3500.00, 'category': 'Eletrônicos'}

# Bad Practice: Código copiado e colado com pequenas diferenças
def mostrar_detalhes_produto(produto):
    print(f"Nome: {produto['name']}")
    print(f"Preço: R${produto['price']:.2f}")
    print(f"Categoria: {produto['category']}")

def mostrar_resumo_produto(produto):
    print(f"Nome: {produto['name']}")
    print(f"Preço: R${produto['price']:.2f}")

# Good Practice: Uma função reutilizável com parâmetros
def exibir_info_produto(produto, mostrar_detalhes=False):
    """Exibe informações de um produto, com opção para detalhes completos."""
    print(f"Nome: {produto['name']}")
    print(f"Preço: R${produto['price']:.2f}")
    if mostrar_detalhes:
        print(f"Categoria: {produto['category']}")

# Uso da boa prática:
print("Resumo do produto (bom):")
exibir_info_produto(produto_exemplo)
print("\nDetalhes do produto (bom):")
exibir_info_produto(produto_exemplo, mostrar_detalhes=True)


# --- Exemplo 5: Evitar "Números Mágicos" ---
print("\n--- Exemplo 5: Evitar Números Mágicos ---")

# Bad Practice: Usar números literais sem explicação
def calcular_imposto_ruim(preco):
    return preco * 0.05 # O que é 0.05?

# Good Practice: Usar constantes nomeadas
TAXA_DE_IMPOSTO_SERVICO = 0.05

def calcular_imposto_bom(preco):
    """Calcula o imposto com base em uma taxa nomeada."""
    return preco * TAXA_DE_IMPOSTO_SERVICO

print(f"Imposto (bom): {calcular_imposto_bom(100):.2f}")


# --- Exemplo 6: List Comprehensions ---
print("\n--- Exemplo 6: List Comprehensions ---")
numeros = [1, 2, 3, 4, 5]

# Bad Practice: Loop 'for' verboso para criar uma nova lista
quadrados_ruim = []
for n in numeros:
    quadrados_ruim.append(n * n)

# Good Practice: List comprehension, mais concisa e legível
quadrados_bom = [n * n for n in numeros]

print(f"Quadrados (bom): {quadrados_bom}")


# --- Exemplo 7: Gerenciadores de Contexto (with) ---
print("\n--- Exemplo 7: Gerenciadores de Contexto ---")

# Bad Practice: Abrir arquivos sem garantir o fechamento
def ler_arquivo_ruim(caminho):
    f = open(caminho, 'r')
    # Se ocorrer um erro aqui, o arquivo nunca será fechado!
    conteudo = f.read()
    f.close() # Pode não ser executado
    return conteudo

# Good Practice: Usar o 'with' para garantir que os recursos sejam liberados
def ler_arquivo_bom(caminho):
    """Lê o conteúdo de um arquivo de forma segura."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."

# Criando um arquivo de teste para o exemplo
with open("teste.txt", "w", encoding='utf-8') as f:
    f.write("Olá, Clean Code!")

print(f"Conteúdo do arquivo (bom): {ler_arquivo_bom('teste.txt')}")
print(f"Tentando ler arquivo inexistente (bom): {ler_arquivo_bom('nao_existe.txt')}")

# Limpando o arquivo de teste
os.remove("teste.txt")