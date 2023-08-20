# fibonacci

class Fibonacci():
    def __init__(self, numero_elementos: int):
        self.numero_elementos = numero_elementos
        

    def sequencia(self, elem: int) -> int:
        if elem <= 1:
            return elem
        else:
            return (self.sequencia(elem-1) + (self.sequencia(elem-2)) )

    # fibonacci resolvido com programação dinâmica     
    def fib_dp(self) -> list:
        dp = [0]*(self.numero_elementos+1)
        dp[0] = 1

        for i in range(1, self.numero_elementos+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[:self.numero_elementos]   

    def __str__(self) -> str:
        '''
        lista = []
        for i in range(1, self.numero_elementos+1):
            lista.append(self.sequencia(i))
        '''
        return str(self.fib_dp())

if __name__ == '__main__':
    print(Fibonacci(10))
