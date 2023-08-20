class EOperacaoNaoPermitida(Exception):
    def __init__(self, mensagem:str):
        self.mensagem = mensagem
    
    def __str__(self):    
        return self.mensagem

class Conta:
    def __init__(self, numerocc: str, saldoinicial:float):
        self.saldo = saldoinicial
        self.numerocc = numerocc
    
    def __str__(self):
        return str(self.saldo)
    
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            raise EOperacaoNaoPermitida('Valor negativo')    

    def sacar(self, valor: float):
        if self.saldo - valor < 0:
            raise EOperacaoNaoPermitida('Saldo não pode ficar negativo')    
        else:
            self.saldo -= valor
        return self.saldo 
    

if __name__ == '__main__':
    conta = Conta('123', 0)
    conta.depositar(100)
    print(conta)
    conta.sacar(10)
    print(conta)
