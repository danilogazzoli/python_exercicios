# -*- coding: utf-8 -*-
from connect import Connection

class Base():
    def __init__(self, tabela:str):
        self.tabela = tabela

    def getInputs(self):
        return {}

    #def __del__(self):
    #    Connection.instance().close()

    def consultar(self, id):
        sql = f'SELECT * FROM {self.tabela} WHERE id = {id} '
        cursor = Connection.instance().select(sql)
        return cursor
    
    def inserir(self, registro: {})-> int:
        columns = ', '.join(registro.keys())
        values = ', '.join(registro.values())
        statement = f'INSERT INTO {self.tabela} ({columns}) VALUES ({values}) RETURNING id;'
        return Connection.instance().insert(statement)
    
    def atualizar(self, id: int, registro: {}) -> int:
        columns = ', '.join(registro.keys())
        values = ', '.join(registro.values())
        statement = f'UPDATE {self.table} SET ({columns}) = ({values}) WHERE id = {id} RETURNING id;'
        return Connection.instance().update(statement)
    
    def excluir(self, id: int):
        statement = f'DELETE FROM {self.tabela} WHERE id={id} RETURNING id'
        return Connection.instance().delete(statement)
        
