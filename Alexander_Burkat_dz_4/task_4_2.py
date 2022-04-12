import requests, sys


def currency_rates():
    cur = sys.argv[1]
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    response = requests.get(url)
    # cur_rub = None
    # return cur_rub
    return response


if __name__ == '__main__':
    print(currency_rates(0))