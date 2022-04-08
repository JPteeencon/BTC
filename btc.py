import cryptocompare as crypto
import datetime

moneda = crypto.get_price('BTC', currency='EUR')
print(moneda)
