# classe data e ano bissexto

from datetime import datetime

class AnoBissexto:
    def __init__(self, data_: datetime):
        self.data_ = data_
    

    def is_ano_bissexto(self):
        ano = self.data_.year
        return  (((ano % 4 == 0) and (ano % 100 != 0)) or 
                 (ano % 400 == 0)) 

if __name__ == '__main__':
    data_ = input('Digite uma data:')
    data_ = datetime.strptime(data_, '%d/%m/%Y')         
    ano_bissexto = AnoBissexto(data_)
    print(ano_bissexto.is_ano_bissexto())


        