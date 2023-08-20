from random import randint


def busca_sequencial(lista: list, item: int) -> tuple[bool, int]:
    idx = 0
    for elemento in lista:
        if elemento == item:
            return True, idx
        idx += 1

    return False, -1    

if __name__ == '__main__':
    lista = []

    for i in range(100):
        lista.append(randint(0,15))

    sorteio = randint(0,20)
    print(f'Número sorteado: {sorteio}')
    print(f'lista: {lista}')
    print(busca_sequencial(lista, sorteio))

