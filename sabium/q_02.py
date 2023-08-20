from datetime import datetime


def month_intTostr(month: int):
    if month == 1:
        return 'Janeiro'
    elif month == 2:
        return 'Fevereiro'
    elif month == 11:
        return 'Novembro'
    else:
        return 'mês inexistente'


if __name__ == '__main__':
    data_ = str(input('Informe a data:'))

    data_ = datetime.strptime(data_, "%d/%m/%Y")

    print(month_intTostr(data_.month))

    print(data_)