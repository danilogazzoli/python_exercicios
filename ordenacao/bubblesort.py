from random import randint

class BubbleSort():
    def __init__(self, vetor):
        self.vetor = vetor
        if not len(self.vetor):
            self.gera_vetor_random()

    def gera_vetor_random(self):
        for i in range(0, 10):
            self.vetor.append(randint(0,100))

    
    def ordena_vetor(self):
        for i in range(0, len(self.vetor) -1):
            for j in range(0, len(self.vetor) - i - 1):
                aux = self.vetor[j]
                if aux > self.vetor[j+1]:
                    self.vetor[j] = self.vetor[j + 1]
                    self.vetor[j + 1] = aux
        return self.vetor            
                    
if __name__ == '__main__':
    bubble = BubbleSort([])    
    print(bubble.ordena_vetor())    