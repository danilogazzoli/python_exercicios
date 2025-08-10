# -*- coding: utf-8 -*-

import numpy as np

def calcular_probabilidade_numero_em_matriz(numero_desejado, tamanho_matriz, numero_experimentos):
    total_ocorrencias = 0
    total_celulas = tamanho_matriz[0] * tamanho_matriz[1]
    
    for _ in range(numero_experimentos):
        matriz = np.random.randint(1, 10, size=tamanho_matriz)
        total_ocorrencias += np.sum(matriz == numero_desejado)
    
    return total_ocorrencias / (total_celulas * numero_experimentos)

def main():
    numero_desejado = int(input("Digite o número que deseja calcular a probabilidade de ser incluído na matriz: "))
    tamanho_matriz = (3, 3)  # Matriz 3x3
    numero_experimentos = 10000  # Número de experimentos
    
    probabilidade = calcular_probabilidade_numero_em_matriz(numero_desejado, tamanho_matriz, numero_experimentos)
    
    print(f"A probabilidade de o número {numero_desejado} estar na matriz é de aproximadamente {probabilidade:.2%}")

if __name__ == "__main__":
    main()
