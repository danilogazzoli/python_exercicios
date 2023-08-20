import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


class Connection():
    _instance = None
    def __init__(self) -> None:
        self.host = os.getenv('host')
        self.port = os.getenv('port')
        self.dbname = os.getenv('dbname')
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        self.conn = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance    
    
    @property
    def connection(self):
        if not self.conn:
            connection_str = f'host={self.host} port={self.port} dbname={self.dbname} user={self.user} password={self.password}'
            self.conn = psycopg2.connect(connection_str)
        return self.conn  
    
    def execute(self, statement):
        cursor = self.connection.cursor()
        cursor.execute(statement)
        lastid = cursor.fetchone()[0]
        self.connection.commit()
        return lastid
    
    def insert(self, statement: str):
        return self.execute(statement)
    
    def insertmany(self, statement: str, tuples=()):
        cursor = self.connection.cursor()
        return cursor.executemany(statement, tuples)

    def select(self, query:str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor
    
    def delete(self, statement: str):
        return self.execute(statement)

    def update(self, statement: str):
        return self.execute(statement)
    
    def close(self):
        print('conexão será fechada.')
        return self.conn.close()

    