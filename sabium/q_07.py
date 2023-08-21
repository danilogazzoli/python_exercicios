

class Jogo_da_Velha:
    """
    Classe que representa o jogo da velha
    """

    def __init__(self):
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]
        self.vencedor = None

    def exibe_tabuleiro(self):
        for i in range(0, len(self.tabuleiro)):
            print(self.tabuleiro[i])

    def get_column(self, matrix, column_index):
        return [row[column_index] for row in matrix]



    def check_diagonais(self):
        # checa as diagonais:
        diagonal1 = []
        diagonal2 = []
        diag_int1 = 0
        diag_int2 = 2
        for i in range(0, len(self.tabuleiro)):
            diagonal1.append(self.tabuleiro[i][diag_int1])
            diagonal2.append(self.tabuleiro[i][diag_int2])
            diag_int1 += 1
            diag_int2 -= 1   

        if diagonal1[0] != None and diagonal1.count(diagonal1[0]) == len(diagonal1):
            self.vencedor = diagonal1[0]
            return True
        if diagonal2[0] != None and diagonal2.count(diagonal2[0]) == len(diagonal2):
            self.vencedor = diagonal2[0]
            return True

        return False
    
    def check_columns(self):
        # checa as colunas:
        for i in range(0, len(self.tabuleiro)):
            columns = self.get_column(self.tabuleiro, i)
            if columns[0] != None and columns.count(columns[0]) == len(columns):
                self.vencedor = columns[0]
                return True
        return False        
            
    def check_linhas(self):
        # checa as linhas:
        for i in range(0, len(self.tabuleiro)):
            linha = self.tabuleiro[i]
            if linha[0] != None and linha.count(linha[0]) == len(linha):
                self.vencedor = linha[0]
                return True
        return False
                
    def check_jogo_terminado(self):

        if self.check_linhas():
            return True
            
        if self.check_columns():
            return True

        if self.check_diagonais():
            return True
 
        return False

   
    def preenche_celula(self, jogador, linha, coluna):
        if self.tabuleiro[linha-1][coluna-1] == None:
            self.tabuleiro[linha-1][coluna-1] = jogador
            return True
        else:
            print('Linha já ocupada pelo outro jogador')    
            return False

if __name__ == '__main__':
    jogo = Jogo_da_Velha()
    jogador_vez = 1
    while not jogo.check_jogo_terminado():
        while True:
            jogo.exibe_tabuleiro()
            print(f'jogador da vez:{jogador_vez}')
            linha = int(input('linha  :'))
            coluna = int(input('coluna:'))
            if jogo.preenche_celula(jogador_vez, linha, coluna):
                break
        jogador_vez = 1 if jogador_vez == 2 else 2
    
    jogo.exibe_tabuleiro()
    print(f'jogo terminado, vencedor: {jogo.vencedor}')    


