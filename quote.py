import json
import pprint
import requests

def get_stock_quote(ticker_symbol):
    payload = {'q': ticker_symbol}
    resp = requests.get("http://finance.google.com/finance/info", params=payload)
    # print(resp.url)
    # print(resp.encoding)
    # print(resp.text)
    return json.loads(''.join([x for x in resp.text if x not in ('/', '[', ']')]))

if __name__ == '__main__':
    quote = get_stock_quote('PANW')
    # print(type(quote))
    print('ticker %s' % quote['t'])
    print('current price %s' % quote['l_cur'])
