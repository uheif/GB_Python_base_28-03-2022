import requests
from decimal import Decimal
import datetime


def currency_rates(cur):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    content = response.text
    serv_time = content.split('Date=')[1].split('"')[1]
    serv_time = datetime.datetime.strptime(serv_time, '%d.%m.%Y').date()
    cusrs = content.split('<CharCode>')
    for el in cusrs:
        if el[:3] == cur.upper():
            value = Decimal(el.split('Value')[1].strip('<>/').replace(',', '.'))
            break
        else:
            value = None

    return value, serv_time


if __name__ == '__main__':
    print(currency_rates('UsD'))