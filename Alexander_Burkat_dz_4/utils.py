import requests
from decimal import Decimal
from datetime import datetime


def currency_rates(cur):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    content = requests.get(url).text
    _serv_date = content.split('Date=')[1].split('"')[1]
    serv_date = datetime.strptime(_serv_date, '%d.%m.%Y').date()
    cur = cur.upper()
    if cur in content:
        _value = content.split(cur)[1].split('Value')[1].strip('></').replace(',', '.')
        value = Decimal(_value).quantize(Decimal('1.00'))
    else:
        value = None

    return value, serv_date


if __name__ == '__main__':
    print(*currency_rates('UsD'), sep=', ')  # 79.85, 2022-04-14
    print(*currency_rates('EUR'), sep=', ')  # 86.72, 2022-04-14
    print(*currency_rates('tuf'), sep=', ')  # None, 2022-04-14
