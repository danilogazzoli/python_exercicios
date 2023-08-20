# -*- coding: utf-8 -*-

from base import Base

class Produto(Base):
    def __init__(self):
        super().__init__('glb.produto')
    
    def getInputs(self):
        descricao = input('Descrição:')
        pesobruto = float(input('Peso bruto:'))
        pesoliquido = float(input('Peso líquido:'))
        return {'descricao': f"'{descricao}'", 
                'pesobruto': str(pesobruto), 
                'pesoliquido':str(pesoliquido)
                }    


