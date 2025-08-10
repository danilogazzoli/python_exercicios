# -*- coding: utf-8 -*-

import random

def calcular_probabilidade_lancamento_dado(numero_desejado, numero_lancamentos):
    ocorrencias = 0
    for _ in range(numero_lancamentos):
        resultado_lancamento = random.randint(1, 6)  # Lanca um dado de seis lados
        if resultado_lancamento == numero_desejado:
            ocorrencias += 1
    return ocorrencias / numero_lancamentos

def main():
    numero_desejado = int(input("Digite o numero que deseja calcular a probabilidade de obter: "))
    numero_lancamentos = int(input("Digite o numero de lancamentos do dado: "))
    
    probabilidade = calcular_probabilidade_lancamento_dado(numero_desejado, numero_lancamentos)
    
    print(f"A probabilidade de obter o numero {numero_desejado} em {numero_lancamentos} lancamentos e de aproximadamente {probabilidade:.2%}")

if __name__ == "__main__":
    main()
