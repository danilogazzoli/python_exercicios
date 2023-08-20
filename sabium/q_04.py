#coding: utf-8

from q_03 import is_numero_primo

if __name__ == '__main__':
    for i in range(100, 200): #o range vai até 199, desconsidera o 200
        if is_numero_primo(i):
            print(f"É número primo: {i}")