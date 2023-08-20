# -*- coding: utf-8 -*-

## determinar o grau de obesidade de uma pessoa
class Obesidade:
    '''
    classe para calcular o índice de massa corporal
    '''
    def __init__(self, peso: float, altura:float):
        self.peso = peso
        self.altura = altura

    @property
    def resultado(self) -> [str, float]:
        imc = self.peso / self.altura**2

        if imc < 26:
            return 'Normal', imc
        elif (imc >= 26) and (imc < 30):
            return 'Obeso', imc
        else:
            return 'Obeso mórbido', imc


    
if __name__ == '__main__':
    peso = float(input("Informe o peso:").replace(',','.'))
    altura = float(input("Informe a altura:").replace(',','.'))
    obesidade_ = Obesidade(peso, altura)
    print(obesidade_.resultado[0])

