# -*- coding: utf-8 -*-

from produto import Produto
from filial import Filial


class App():
    def __init__(self):
        self.base = None

    def consultar(self, id: int = None):
        if id == None:
            id = int(input('Digite o cÃ³digo:'))
        cursor = self.base.consultar(id)
        for record in cursor:
            print(record)
            return record[0]
        else:
            print(f'Registro {id} não encontrado ou excluído.')
        return None
    
    def getInputs(self):
        return self.base.getInputs()

    def inserir(self):
        return self.base.inserir(self.getInputs())
    
    def atualizar(self):
        id = self.consultar()
        if id:
            id = self.base.atualizar(id, self.getInputs())
            self.consultar(id)
        return id
    
    def excluir(self):
        id = self.consultar()
        if id:
            opt = input('Deseja excluir? (S/N)')
            if opt.upper() == 'S':
                return self.base.excluir(id)
        return id
            

    def run(self):
        while True:
            opt = int(input('<1> Produto <2> Filial <5> Sair: '))
            if opt == 1:
                self.base = Produto()
            elif opt == 2:
                self.base = Filial()
            elif opt == 5: 
                break   
            else:
                opt = -1
                print('Opção inválida')        
            if opt in [1,2]:   
                opt = int(input('Opções: <1> Inserir <2> Atualizar <3> Excluir <4> Consultar <5> Sair: '))
                if opt == 5:
                        break
                elif opt == 1:
                        id = self.inserir()
                        print(f'Id inserido: {id}')
                elif opt == 2:
                        id = self.atualizar()  
                elif opt == 3:
                        id = self.excluir()
                        self.consultar(id)
                elif opt == 4: 
                        self.consultar()   
                else:
                        print('Opção não encontrada.')


if __name__ == '__main__':
    app = App()
    app.run()


