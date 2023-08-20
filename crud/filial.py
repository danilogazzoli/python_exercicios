# -*- coding: utf-8 -*-

from base import Base

class Filial(Base):
    def __init__(self):
        super().__init__('glb.filial')
    
    def getInputs(self):
        descricao = input('Nome:')
        return {'fantasia': f"'{descricao}'"}
