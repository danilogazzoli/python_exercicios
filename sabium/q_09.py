from q_08 import AnoBissexto
from datetime import datetime, timedelta

class DataIncrementada(AnoBissexto):
    def __init__(self, data_: datetime):
        super().__init__(data_)

    def count_month_days(self):
        mes = self.data_.month
        if mes == 2:
            if self.is_ano_bissexto():
                return 29
            else:
                return 28
        elif mes in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30    
    
    def __str__(self):    
        return str(self.data_.strftime('%d/%m/%Y') )
    
    def inc_days(self, number: int):
        self.data_ = self.data_ + timedelta(days=number)
        return self.data_
    
if __name__ == '__main__':
    data_ = input('Digite uma data:')
    data_ = datetime.strptime(data_, '%d/%m/%Y')         
    ano_bissexto = DataIncrementada(data_)
    print(ano_bissexto)
    print(ano_bissexto.count_month_days())
    ano_bissexto.inc_days(-20)
    print(ano_bissexto)
