#coding: utf-8


def count_numero_primo(numero: int):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont += 1
        if cont > 2: 
            break    
    return cont

def is_numero_primo(numero: int):
    return count_numero_primo(numero) == 2

if __name__ == '__main__':
    numero = int(input('Entre com o número:'))

    if is_numero_primo(numero):
        print('sim')
    else:
        print('não é')    

