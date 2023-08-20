# encoding: utf_8

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






