

class Empregado:
    """
    Classe que representa os empregados da empresa
    """

    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario if salario > 0 else 0

        
    def aumenta_salario(self, percentual_aumento: float):
        self.salario = self.salario + self.salario * (percentual_aumento /100)

    

if __name__ == '__main__':
    lista_empregados = []
    for i in range(0,3):
        nome = str(input(f'Digite o nome do empregado {i}:'))
        salario = float(input(f'Digite o salário do empregado {i}:'))
        lista_empregados.append(Empregado(nome, salario))

    percentual_aumento = float(input('Digite o aumento %:'))

    for empregado in lista_empregados:
        empregado.aumenta_salario(percentual_aumento)
        print(f'Empregado: {empregado.nome}, novo salario: {empregado.salario}')    




    
