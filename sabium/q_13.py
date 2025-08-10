# -*- coding: utf-8 -*-


#preciso de um programa em python que me diga qual é a probabilidade de um número ser incluído em uma matriz bidimensional 3x 3

import random
import numpy as np


def gerar_matriz_aleatoria():
    return [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    #return np.random.randint(1,10, size=(3, 3))

def calcular_probabilidade(matriz, numero):
    total_ocorrencias = sum(row.count(numero) for row in matriz)
    total_celulas = len(matriz) * len(matriz[0])
    return total_ocorrencias / total_celulas

def main():
    matriz = gerar_matriz_aleatoria()
    print("Matriz gerada:")
    for row in matriz:
        print(row)
    numero = int(input("Digite o numero para calcular a probabilidade de ocorrência: "))
    probabilidade = calcular_probabilidade(matriz, numero)
    print(f"A probabilidade de o numero {numero} ocorrer na matriz eh de {probabilidade:.2%}")

if __name__ == "__main__":
    main()
