# DIFERENÇA ENTRE LISTAS E ARRAYS
# LISTAS:

# Tipo de Dados: Heterogênea. Pode conter elementos de diferentes tipos de dados na mesma lista (ex: inteiros, strings, outros objetos).
# Uso de Memória: Menos eficiente. Cada elemento na lista é um objeto Python completo, e a lista armazena ponteiros para esses objetos. Isso adiciona uma sobrecarga de memória.
# Funcionalidade: Possui uma vasta gama de métodos embutidos e é extremamente flexível para operações do dia a dia (adicionar, remover, fatiar, etc.).
# Uso: É a escolha padrão para a maioria dos casos de uso que envolvem uma coleção de itens.

# ARRAYS:

# Tipo de Dados: Homogênea. Todos os elementos devem ser do mesmo tipo (ex: todos inteiros).
# Uso de Memória: Mais eficiente. Os arrays armazenam os dados de forma contígua na memória, o que reduz a sobrecarga.
# Funcionalidade: Possui um conjunto mais limitado de operações em comparação com listas, mas é mais rápido para operações de acesso e modificação.
# Uso: Ideal para situações em que o desempenho é crítico e os dados são homogêneos.

# Uma lista pode conter diferentes tipos de dados
minha_lista = [1, "gato", 3.14, True, [10, 20]]

print(f"Lista: {minha_lista}")
print(f"Tipo do primeiro elemento: {type(minha_lista[0])}")
print(f"Tipo do segundo elemento: {type(minha_lista[1])}")

minha_lista.append("novo item")
print(f"Lista após adicionar item: {minha_lista}")

# array:

import array

# O módulo array do Python, que você usou no seu arquivo list_array.py, é projetado para ser uma estrutura de dados de alta performance e baixo consumo de memória para tipos numéricos primitivos (como inteiros e floats).
# Ele não suporta strings como um tipo de dado. O mais próximo que ele chega é o código de tipo 'u', que armazena um único caractere Unicode, não uma string de comprimento variável.

# Criando um array de inteiros ('i' é o código de tipo para signed int)
meu_array = array.array('i', [10, 20, 30, 40, 50])

print(f"Array: {meu_array}")
print(f"Tipo do array: {type(meu_array)}")

# Adicionando um novo item (deve ser do mesmo tipo)
meu_array.append(60)
print(f"Array após adicionar item: {meu_array}")

# Tentar adicionar um tipo diferente resultará em um erro
try:
    meu_array.append("gato")
except TypeError as e:
    print(f"\nErro ao tentar adicionar string: {e}")

# NumPy ndarray

import numpy as np

# Cria um array NumPy a partir de uma lista
array_numpy = np.array([10, 20, 30, 40, 50])

print(f"Array NumPy: {array_numpy}")
print(f"Tipo do array: {type(array_numpy)}")

# A grande vantagem são as operações vetorizadas (aplicadas a todos os elementos de uma vez)
array_multiplicado = array_numpy * 2
print(f"Array multiplicado por 2: {array_multiplicado}")

#
# --- Tabela Comparativa Rápida ---
#
# Característica | list                         | array.array                  | numpy.ndarray
# -----------------------------------------------------------------------------------------------------------------
# Tipo de Dados  | Heterogêneo                  | Homogêneo (numérico)         | Homogêneo (geralmente numérico)
# Uso de Memória | Alto                         | Baixo                        | Baixo
# Performance    | Menor para operações numéricas| Razoável para armazenamento  | Altíssima para operações numéricas
# Flexibilidade  | Muito alta                   | Baixa                        | Alta (para dados numéricos)
# Dimensionalidade| Unidimensional (pode aninhar)| Unidimensional               | Multidimensional
# Biblioteca     | Embutida                     | Módulo `array`               | Biblioteca `numpy` (externa)
# Caso de Uso    | Coleções de uso geral        | Armazenamento compacto       | Computação científica/Análise de dados
#
