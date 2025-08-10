# encoding: utf_8

from collections import deque

def is_palindromo_deque(palavra:str):
    chardeque = deque(palavra)
    #for letra in palavra:
    #    chardeque.append(letra)
    stillequal = True

    while len(chardeque) > 1 and stillequal:
        primeira = chardeque.popleft()
        ultima = chardeque.pop()
        stillequal = primeira == ultima
    return stillequal

def is_palindromo(palavra: str):
    reversed = palavra[::-1]
    return reversed.upper() == palavra.upper()

if __name__ == '__main__':
    palavra = str(input('Digite a palavra:'))


    resultado = 'sim' if is_palindromo(palavra) else 'não'

    print(resultado)

    '''
    if is_palindromo(palavra):
        print('é')
    else:
        print('nao é')    
    '''






